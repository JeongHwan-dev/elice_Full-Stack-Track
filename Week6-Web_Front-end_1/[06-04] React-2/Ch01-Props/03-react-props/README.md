# Props

Props는 컴포넌트 값을 전달하는 역할을 수행한다.

컴포넌트는 Props를 수정할 수 없는 순수 함수로 정의된다.

**순수함수 예시**

```javascript
function sum(a, b) {
  return a + b;
}
```

**순수함수가 아닌 예시**

```javascript
function withdraw(account, amount) {
  account.total -= amount;
}
```

Props는 컴포넌트 호출 시, 인자값의 이름과 내용을 함께 제공한다.

컴포넌트 내에서 props.[이름]의 형식으로 인자값을 받아 사용한다.

**Props 예시**

```javascript
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <div>영화: {props.name}</div>
      <div>한줄평: {props.text}</div>
    </div>
  );
}

const element = (
  <div>
    <UserInfo name="겨울왕국" text="엘사가 너무 예뻐요!" />
    <UserInfo name="신과함께" text="배우님 연기력 최고" />
  </div>
);
```
