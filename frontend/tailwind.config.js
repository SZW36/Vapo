/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#222629",
        secondary: "#86C232",
      },
    },
    fontFamily: {
      profile: ["Montserrat"],
    },
  },
  plugins: [],
};
