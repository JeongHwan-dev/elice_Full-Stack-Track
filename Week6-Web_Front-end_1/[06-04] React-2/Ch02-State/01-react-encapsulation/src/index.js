import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

// 현재 시간을 출력하는 컴포넌트
// 현재 시간의 props를 받아 출력합니다.
function Clock(props) {
  return (
    <div>
      <h1>Hello, World!</h1>
      <h2>현재 시간: {props.date.toLocaleTimeString()}</h2>
    </div>
  );
}

// 매초 마다 호출되는 함수
function tick() {
  // Clock 컴포넌트를 호출
  const element = <Clock date={new Date()} />;

  // ReactDOM에 element를 렌더링
  ReactDOM.render(element, document.getElementById("root"));
}

setInterval(tick, 1000);
