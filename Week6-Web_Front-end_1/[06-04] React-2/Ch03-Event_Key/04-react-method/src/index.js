import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

class EventClass extends React.Component {
  constructor(props){
    super(props);
    // 정의한 이벤트를 바인딩합니다.
    this.handleClick = this.handleClick.bind(this);
  }

  // handleClick 이벤트를 정의합니다. 인자값을 받아 alert()을 출력합니다.
  handleClick = (data) => {
    alert("전달받은 인자값: " + data);
  }
  
  render() {
    var data = "ABCDEFG";
    return (
      // data값을 인자값으로 제공하는 이벤트 핸들러를 작성합니다.
      <button onClick={this.handleClick.bind(this, data)}>버튼을 눌러주세요!</button>
    );
  }
}

ReactDOM.render(<EventClass />, document.getElementById('root'));

