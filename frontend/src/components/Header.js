import React from "react";

function Header() {
  return (
    <div className="pt-4 h-[10vh] w-screen bg-primary flex">
      <div className="h-[8vh] w-[96vw] mx-auto my-auto px-20 bg-gray-100 flex flex-row items-center rounded-md">
        <h1 className="font-bold text-3xl">VAPO</h1>
        <div className="grow"></div>
        <div class="relative w-10 h-10 overflow-hidden bg-white rounded-full dark:bg-gray-600">
          <svg
            class="absolute w-12 h-12 text-gray-400 -left-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
      </div>
    </div>
  );
}

export default Header;
