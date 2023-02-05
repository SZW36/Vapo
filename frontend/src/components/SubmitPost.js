import React, { useState } from "react";
import { MdOutlineTransitEnterexit } from "react-icons/md";
import URL from "./url";
import { useRecoilValue } from "recoil";
import { userID } from "./atoms";

function SubmitPost({ addPost }) {
  const [show, setShow] = useState(false);
  const [text, setText] = useState("");

  const userIDValue = useRecoilValue(userID);

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/create_post", {
      method: "POST",
      headers: {
        Accepts: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: userIDValue.id, content: text }),
    })
      .then((res) => res.json())
      .then(() => {});
    addPost({ user_id: userIDValue.id, content: text });
    setText("");
    setShow(false);
  }

  return (
    <div className="h-[7vh] mt-10 mx-10 py-6 px-4 bg-white rounded-md flex justify-center items-center">
      <div className="flex flex-row space-x-3">
        <input
          onClick={() => setShow(true)}
          placeholder="Click"
          className="border-2 focus:outline-none rounded-md"
        />
        <button className="text-sm font-thin">Share Your Thoughts</button>
      </div>

      {show && (
        <div className="fixed inset-0 z-20 bg-gray-300 bg-opacity-75 transition-opacity flex justify-center items-center">
          <div className="w-[40vw] bg-white rounded-md">
            <div className="h-10 w-full flex justify-end">
              <MdOutlineTransitEnterexit
                onClick={() => setShow(false)}
                size={30}
                className="text-gray-500 hover:text-black ease-in-out duration-300"
              />
            </div>
            <h2 className="text-center text-4xl font-semibold">Share</h2>
            <form
              onSubmit={(e) => handleSubmit(e)}
              className="flex flex-col space-y-6 p-10"
            >
              <textarea
                placeholder="Share your thougths for the day!"
                className="focus:outline-none py-2 px-2 border-2 border-primary rounded-md"
                value={text}
                onChange={(e) => setText(e.target.value)}
              />
              <button
                className={`${
                  text.length === 0 ? "bg-gray-300" : "bg-primary"
                } w-full py-2 rounded-md text-white`}
                disabled={text.length === 0}
              >
                Submit Post
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default SubmitPost;
