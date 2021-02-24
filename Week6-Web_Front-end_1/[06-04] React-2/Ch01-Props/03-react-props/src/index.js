import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// 프로필 출력 컴포넌트
function Profile(props) {
  return (
    <div>
      <h2>이름: {props.name}</h2>
      <h2>나이: {props.age}</h2>
      <h2>성별: {props.gender}</h2>
    </div>
  );
}

// 데이터 저장 변수
const data = {
  name: 'Joshi',
  age: '25',
  gender: '남'
};

const element = (
  <Profile name={data.name} age={data.age} gender={data.gender} />
);

ReactDOM.render(element, document.getElementById('root'));