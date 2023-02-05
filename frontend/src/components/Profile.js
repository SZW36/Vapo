import React from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import ProgressProvider from "./ProgressProvider";
import CountUp from "react-countup";
import URL from "./url";

function Profile() {
  // const [username, setUsername] = useState("");
  // const [value, setValue] = useState(0)

  // useEffect(() => {
  //   fetch(`${URL}/`)
  //     .then((res) => res.json())
  //     .then(setUsername);
  //   fetch(`${URL}/`)
  //     .then((res) => res.json())
  //     .then(setValue);
  // }, []);

  const value = 72;

  return (
    <div className="mt-10 absolute left-[2vw] h-[80vh] w-[23vw] bg-gray-50 rounded-md flex flex-col">
      <h2 className="mt-10 text-center text-4xl font-light text-gray-500">
        Kota
      </h2>
      <div className="p-14">
        <ProgressProvider valueStart={0} valueEnd={value}>
          {(percentage) => (
            <CircularProgressbar
              value={percentage}
              text={`${percentage}%`}
              styles={buildStyles({
                textSize: "16px",
                pathTransitionDuration: 1,
                textColor: "#86C232",
                trailColor: "#d6d6d6",
                pathColor: `rgba(34, 38, 41, ${percentage / 100})`,
              })}
            />
          )}
        </ProgressProvider>
      </div>
      <div className="ml-10 flex flex-col space-y-3">
        <h2 className="font-thin text-lg">Total Users Registered Today: </h2>
        <CountUp
          className="text-center text-secondary"
          duration={1}
          end={245432}
        />
        <h2 className="font-thin text-lg">Succesful People Today!</h2>
        <CountUp
          className="text-center text-secondary"
          duration={1}
          end={10234}
        />
      </div>
    </div>
  );
}

export default Profile;
