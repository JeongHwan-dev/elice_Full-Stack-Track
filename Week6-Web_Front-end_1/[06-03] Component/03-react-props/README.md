# Props

Props는 컴포넌트에 값을 전달하는 역할을 수행합니다.

컴포넌트는 Props를 수정할 수 없는 순수 함수로 정의됩니다.

(순수함수란 입력값이 바뀌지 않고 항상 동일한 입력값에 대해 동일한 출력값을 제공하는 함수입니다.)

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

위는 함수 내 인자값인 accout의 값을 변경하려 하기 때문에 순수함수가 아닙니다.

Props는 컴포넌트 호출 시, 인자값의 이름과 내용을 함께 제공합니다.

컴포넌트 내에서 props.[이름]의 형식으로 인자값을 받아 사용합니다.

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
