import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function ActionLink() {
  // 이벤트를 등록합니다.
  function handleClick(e) {
    console.log("The link was clicked.");
    alert("버튼이 클릭되었습니다.")
  }
  // a 태그에 이벤트를 등록합니다.
  return (
    <a href="#" onClick={handleClick}>Click me</a>
  );
}

ReactDOM.render(<ActionLink />, document.getElementById('root'));