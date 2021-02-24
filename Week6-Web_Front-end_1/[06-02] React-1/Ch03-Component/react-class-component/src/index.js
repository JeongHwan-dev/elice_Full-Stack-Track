import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

// 클래스 컴포넌트

// 정의된 이름
const name = "Sara";

// 클래스명이 Welecome인 컴포넌트를 작성합니다.
class Welcome extends React.Component {
  render() {
    return <h2>Welecome, {name}!</h2>;
  }
}

// 컴포넌트를 호출하여 element에 저장합니다.
const element = <Welcome />;

ReactDOM.render(element, document.getElementById("root"));
