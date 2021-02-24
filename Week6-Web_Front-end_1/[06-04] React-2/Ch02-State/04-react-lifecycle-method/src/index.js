import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

class Clock extends React.Component {
  constructor(props) {
    console.log("constructor() 호출");
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    console.log("componentDidMount() 호출");
    this.timerID = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    console.log("componentWillUnmount() 호출");
    clearInterval(this.timerID);
  }

  tick() {
    console.log("tick() 호출");
    this.setState({date: new Date()});
  }

  render() {
    console.log("render() 호출");
    return(
      <div>
        <h1>Hello, World!</h1>
        <h2>It id {this.state.date.toLocaleTimeString()}</h2>
      </div>
    );
  }
}

ReactDOM.render(<Clock />, document.getElementById('root'));