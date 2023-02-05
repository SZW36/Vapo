import React, { useState } from "react";
import { AiOutlineLike, AiOutlineComment } from "react-icons/ai";
import { BsEmojiLaughing } from "react-icons/bs";

function Post({ id, show, setShow, username, content, date }) {
  const [commentClicked, setCommentClicked] = useState(false);
  const [likeClicked, setLikeClicked] = useState(false);
  const [laughClicked, setLaughClicked] = useState(false);

  return (
    <div className="bg-white mx-10 py-4 px-6 rounded-md drop-shadow-lg flex flex-col space-y-4">
      <div className="flex flex-row space-x-2 items-center">
        <img
          className="w-10 h-10 rounded-full"
          src="https://newprofilepic2.photo-cdn.net//assets/images/article/profile.jpg"
          alt="Rounded avatar"
        />
        <div>
          <h3 className="text-base">{username}</h3>
          <p className="text-xs text-gray-500">{date}</p>
        </div>
      </div>
      <div>
        <p>{content}</p>
      </div>
      <div className="flex flex-row space-x-3">
        <button
          onClick={() => {
            if (commentClicked) {
              setShow(0);
            } else {
              setShow(id);
            }
            setCommentClicked(!commentClicked);
          }}
          className={`${
            commentClicked ? "bg-secondary hover:bg-secondary" : ""
          } w-1/2 iconButton flex justify-center`}
        >
          <AiOutlineComment size={20} />
        </button>
        <div className="w-[30%]"></div>
        <button className="iconButton">
          <AiOutlineLike size={20} />
        </button>
        <button className="iconButton">
          <BsEmojiLaughing size={20} />
        </button>
      </div>
    </div>
  );
}

export default Post;
