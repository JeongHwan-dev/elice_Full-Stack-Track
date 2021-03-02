# 함수 컴포넌트를 클래스로 변환

함수 컴포넌트는 State를 가질 수 없다는 단점이 있다.

이를 해결하기 위해서 함수 컴포넌트를 클래스 컴포넌트로 변환하는 과정이 필요하다.

### 변환 과정

    1. React.Component 를 상속받는 컴포넌트 클래스 생성
    2. 메소드 명이 render() 인 빈 메소드 추가
    3. 함수 컴포넌트 내용을 render() 메소드로 이동
    4. render() 안의 props를 this.props 로 변경
    5. 기존의 함수 컴포넌트 삭제

### 컴포넌트 변환 예시

**함수 컴포넌트**

```javascript
function Hello(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

**클래스 컴포넌트**

```javascript
class Hello extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
