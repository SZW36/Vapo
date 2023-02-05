import React, { useState, useEffect } from "react";
import SubPosts from "./SubPosts";
import URL from "./url";

function SubFeed({ show }) {
  const [reply, setReply] = useState("");

  const [subPosts, setSubPosts] = useState([]);

  useEffect(() => {
    fetch("/get_sub_post", {
      method: "POST",
      headers: {
        Accepts: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ post_id: show }),
    })
      .then((res) => res.json())
      .then((data) => {
        setSubPosts(data);
      });
  }, [show]);

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/create_sub_post", {
      method: "POST",
      headers: {
        Accepts: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ post_id: show, content: reply }),
    })
      .then((res) => res.json())
      .then(() => {
        setSubPosts((subPosts) => [
          { post_id: show, content: reply },
          ...subPosts,
        ]);
      });
    setReply("");
  }

  return (
    <div
      className={`${
        show !== 0 ? "translate-x-0" : "translate-x-[200%]"
      } ease-in-out duration-1000 mt-10 absolute right-[2vw] h-[80vh] w-[23vw] bg-white rounded-md`}
    >
      <div className="h-[60vh] w-full flex flex-col overflow-y-scroll">
        {subPosts.map(({ id, username, content, date }) => {
          return (
            <SubPosts
              key={id}
              username={username}
              content={content}
              date={date}
            />
          );
        })}
      </div>
      <div className="h-[20vh] w-full p-10 flex justify-center items-center">
        <form
          onSubmit={(e) => handleSubmit(e)}
          className="flex flex-row space-x-2"
        >
          <textarea
            value={reply}
            onChange={(e) => setReply(e.target.value)}
            className="focus:outline-none border-2 p-2 border-primary rounded-md"
          />
          <button className="px-4 py-2 bg-secondary rounded-md drop-shadow-lg">
            Reply
          </button>
        </form>
      </div>
    </div>
  );
}

export default SubFeed;
