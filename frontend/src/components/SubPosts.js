import React from "react";

function SubPosts({ username, content, date }) {
  return (
    <div className="my-3 w-[90%] mx-auto p-4 bg-primary rounded-md flex flex-col space-y-2">
      <div className="flex flex-row space-x-2 items-center justify-end">
        <h3 className="text-xs text-white">{username}</h3>
        <img
          className="w-6 h-6 rounded-full"
          src="https://newprofilepic2.photo-cdn.net//assets/images/article/profile.jpg"
          alt="Rounded avatar"
        />
      </div>
      <div className="flex flex-col items-end">
        <p className="text-white">{content}</p>
        <p className="mt-2 text-secondary text-xs">{date}</p>
      </div>
    </div>
  );
}

export default SubPosts;
