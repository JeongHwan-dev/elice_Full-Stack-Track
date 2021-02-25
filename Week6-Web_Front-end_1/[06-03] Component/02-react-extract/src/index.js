import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

// user의 정보(이름, 프로필 사진) 출력 컴포넌트
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <div>이름: {props.user.name}</div>
      <div>나이: {props.user.age}</div>
    </div>
  );
}

// 코멘트 출력 컴포넌트
function Comment(props) {
  return <div className="Comment">문구: {props.text}</div>;
}

// 문구 출력 컴포넌트
function Profile(props) {
  return (
    <div classNeme="Profile">
      <UserInfo user={props.author} />
      <Comment text={props.text} />
    </div>
  );
}

const comment = {
  text: "I hope you enjoy learning React!",
  author: {
    name: "엘리스 토끼",
    age: "12",
  },
};

const element = <Profile text={comment.text} author={comment.author} />;

ReactDOM.render(element, document.getElementById("root"));
