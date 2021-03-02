import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

// props 사용 컴포넌트

// 프로필 출력 컴포넌트
// class Profile extends React.Component {
//   render() {
//     return (
//       <div>
//         <h2>이름: {this.props.name}</h2>
//         <h2>나이: {this.props.age}</h2>
//       </div>
//     );
//   }
// }

// // 데이터 저장 변수
// const data = {
//   name: "Joshi",
//   age: "25",
// };

// const element = <Profile name={data.name} age={data.age} />;

// State 사용 컴포넌트

// 프로필 출력 컴포넌트
class Profile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "Joshi",
      age: "25",
    };
  }

  render() {
    return (
      <div>
        <h2>이름: {this.state.name}</h2>
        <h2>나이: {this.state.age}</h2>
      </div>
    );
  }
}

const element = <Profile />;

ReactDOM.render(element, document.getElementById("root"));
