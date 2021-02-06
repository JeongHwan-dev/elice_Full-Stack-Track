import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// 현재 시간을 출력하는 컴포넌트
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: new Date()
    };
  }

  // props를 state로 변경합니다.
  render() {
    return (
      <div>
        <h1>Hello, World!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}</h2>
      </div>
    );
  }
}

// Clock 컴포넌트를 호출
const element = (
  <Clock />
);

ReactDOM.render(element, document.getElementById('root'));