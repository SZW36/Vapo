import React, { useState, useEffect } from "react";
import Post from "./Post";
import Profile from "./Profile";
import SubFeed from "./SubFeed";
import SubmitPost from "./SubmitPost";
import URL from "./url";
import { useRecoilValue } from "recoil";
import { userID } from "./atoms";

function Home() {
  const [show, setShow] = useState(0);
  const userIDValue = useRecoilValue(userID);

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("/get_post", {
      method: "POST",
      headers: {
        Accepts: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: userIDValue.id }),
    })
      .then((res) => res.json())
      .then((data) => {
        setPosts(data);
      });
  }, []);

  function addPost(post) {
    setPosts((posts) => [post, ...posts]);
  }

  return (
    <div className="h-[90vh] w-screen bg-primary flex flex-row">
      <div className="h-full w-[25vw]">
        <Profile />
      </div>
      <div className="h-full w-[50vw] flex flex-col overflow-y-scroll">
        <SubmitPost addPost={addPost} />
        <div className="mt-10 flex flex-col space-y-4">
          {posts.map(({ id, username, content, date }) => {
            return (
              <Post
                key={id}
                id={id}
                show={show}
                setShow={setShow}
                username={username}
                content={content}
                date={date}
              />
            );
          })}
        </div>
      </div>
      <div className="h-full w-[25vw]"></div>
      <SubFeed show={show} />
    </div>
  );
}

export default Home;
