import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

function UserInfo(props) {
  return (
    <div className="UserInfo">
      <div>영화: {props.name}</div>
      <div>한줄평: {props.text}</div>
    </div>
  );
}

const element = (
  <div>
    <UserInfo name="겨울왕국" text="엘사가 너무 예뻐요!" />
    <UserInfo name="신과함께" text="배우님 연기력 최고!" />
  </div>
);

ReactDOM.render(element, document.getElementById("root"));
