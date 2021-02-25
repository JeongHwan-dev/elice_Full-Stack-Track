import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

// 함수 컴포넌트를 사용하여 Subject 컴포넌트를 정의
function Subject(props) {
  return <h3>React를 이해하기 위해서는 {props.name}을(를) 알아야합니다.</h3>;
}

// Curriculum 컴포넌트 정의
function Curriculum() {
  return (
    <div>
      <Subject name="HTML" />
      <Subject name="CSS" />
      <Subject name="JavaScript" />
    </div>
  );
}

ReactDOM.render(<Curriculum />, document.getElementById("root"));
