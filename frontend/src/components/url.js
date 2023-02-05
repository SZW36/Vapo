let URL;

if (process.env.NODE_ENV === "development") {
  URL = "https://localhost:5000";
} else {
  URL = "";
}

export default URL;
