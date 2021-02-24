import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};
    this.handleClick = this.handleClick.bind(this);
  }

  // handleClick 이벤트를 정의합니다.
  handleClick = () => {
    this.setState({
      isToggleOn: false
    });
  }

  render() {
    return (
      // button 태그에 handleClick 이벤트를 등록합니다.
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(<Toggle />, document.getElementById('root'));