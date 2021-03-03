import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

class Clock extends React.Component {
  // 1번째 호출
  constructor(props) {
    console.log("constructor() 호출");
    super(props);
    this.state = { date: new Date() };
  }

  // 3번째 호출
  componentDidMount() {
    console.log("componentDidMount() 호출");
    this.timerID = setInterval(() => this.tick(), 1000);
  }

  // 컴포넌트가 마운트 해제되어 제거되기 직전에 호출
  componentWillUnmount() {
    console.log("componentWillUnmount() 호출");
    clearInterval(this.timerID);
  }

  // 4번째 호출
  tick() {
    console.log("tick() 호출");
    this.setState({ date: new Date() });
  }

  // 2번째 호출
  render() {
    console.log("render() 호출");
    return (
      <div>
        <h1>Hello, World!</h1>
        <h2>It id {this.state.date.toLocaleTimeString()}</h2>
      </div>
    );
  }
}

ReactDOM.render(<Clock />, document.getElementById("root"));
