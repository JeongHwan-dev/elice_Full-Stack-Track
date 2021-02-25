import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

class Change extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 1,
      color: "red",
    };
  }

  changeColor = () => {
    if (this.state.count % 2 === 1) {
      this.setState({ color: "blue" });
    } else {
      this.setState({ color: "red" });
    }
    this.state.count += 1;
  };

  render() {
    return (
      <div>
        <h1>It is a {this.state.color}</h1>
        <button type="button" onClick={this.changeColor}>
          Change color
        </button>
      </div>
    );
  }
}

ReactDOM.render(<Change />, document.getElementById("root"));
