import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

class EventClass extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: 'Hello'
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState({
      message: 'Goodbye!'
    })
  }

  render() {
    return (
      <div>
        <div>{this.state.message}</div>
        <button onClick={this.handleClick}>Click</button>
      </div>
    );
  }
}

ReactDOM.render(<EventClass />, document.getElementById('root'));