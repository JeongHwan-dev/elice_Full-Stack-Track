import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'
import App from './App';

// 함수를 정의합니다.
function output(str1) {
  return str1;
}

// 고객의 이름을 출력하는 함수
function formatName(user) {
  return user.lastName + ' ' + user.firstName;
}

// 인사 문구를 출력하는 함수
function getGreeting(user) {
  return <h1>Hello, {formatName(user)}!</h1>;
}

// name 변수를 선언하고, 이름을 저장합니다.
const name = "Josh Perez";

// 고객의 이름을 저장하는 변수
const user = {
  lastName: '코딩하는',
  firstName: '엘리스'
}

// HTML을 JSX로 변환하여 element에 저장합니다.
// 표현식을 사용하여 name 을 포함합니다.
const element = (
  <div>
    <h2>코더랜드에 오신 것을 환영합니다:)</h2>
    <h2>즐거운 React! 함께 공부해봐요~</h2>
    <hr></hr>
    <h1>Hello, {name}</h1>
    <hr></hr>
    <h2>{output("안녕하세요! 코더랜드에 오신걸 환영합니다.:)")}</h2>
    <hr></hr>
    <h2>{getGreeting(user)}</h2>
    <hr></hr>
    <a href="https://www.naver.com/">네이버로 이동!</a>
    <hr></hr>
    <h2>안녕하세요:)</h2>
    <h2>오늘도 화이팅!!</h2>
  </div>
);


ReactDOM.render(element, document.getElementById('root'));
