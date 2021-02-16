# 01 Redux로 비동기 처리

## Redux 미들웨어

    액션 -> 미들웨어 -> 리듀서 -> 스토어

---

## Redux 미들웨어란?

Redux 미들웨어는 리덕스의 기능을 확장할 때 사용하는 기능

1. 액션 로그를 출력하는 미들웨어
2. 비등기 처리를 하게 해주는 미들웨어
3. 크래시 리포트를 전송하는 미들웨어
4. 라우팅을 위해 사용하는 미들웨어

**이러한 미들웨어가 하는일**

- 특정 조건에 따라 액션이 무시되게 만들 수 있다.
- 액션을 콘솔에 출력하거나, 서버 쪽에 로깅을 할 수 있다.
- 액션이 디스패치 됐을 때 이를 수정해서 리듀서에게 전달되도록 할 수 있다.
- 특정 액션이 발생했을 때 이에 기반하여 다른 액션이 발생되도록 할 수 있다.
- 특정 액션이 발생했을 때 특정 자바스크립트 함수를 실행시킬 수 있다.

---

## Redux 미들웨어 구조

```javascript
const middleware = store => next => action {
console.log('이곳은 "액션이 디스패치 되고 리듀서로 처리가 이동하는 시점의 부분"입니다.');
const result = next(action);
return result;
};
```

리덕스 미들웨어를 일반적인 함수 리터럴로 나타내면 다음과 같은 형태

```javascript
const middleware = function (store) {
  return function (next) {
    return function (action) {
      console.log(
        '이곳은 "액션이 디스패치되고 리듀서로 처리가 이동하는 시점의 부분" 입니다.'
      );
      const result = next(action);
      return result;
    };
  };
};
```

---

## 동기와 비동기

**동기(Sync)**

```
작업을 다른 Thread에서 하도록 시킨 후 그 작업이 끝나길 "기다리고" 다음 일을 진행
```

```javascript
//동기적인 예
console.log("start");
const a = 100;
const b = 200;
const sum = a + b;
console.log("합계 = ${sum}");
console.log("finish");

/*
실행결과
start
합계 = 300
finish
*/
```

**비동기(Async)**

```
작업을 다른 Thread에서 하도록 시킨 후, 그 작업이 끝나길 "안 기다리고" 다음 일을 진행
```

```javascript
//비동기 처리 예
console.log("start");
setTimeout(() => {
  const a = 100;
  const b = 200;
  const sum = a + b;
  console.log("합계 = ${sum}");
}, 1000);
console.log("finish");

/*
실행결과
start
finish
합계 = 300
*/
```

---

## redux-thunk

리덕스를 사용하는 애플리케이션에서 비동기 작업을 처리할 때 가장 기본적인 방법

---

## thunk란?

thunk란 특정 작업을 나중에 하도록 미루기 위해서 함수 형태로 감싼 것

```javascript
const foo = () => 1 + 1;
```

이렇게 하면, 1 + 1의 연산이 코드가 실행될 때 바로 이뤄지지 않고 나중에 foo()가 호출되어야만 이뤄진다.

---

## redux-thunk가 하는 일

- pure javascript object 형태로 action을 반환하던 actionCreator에서 함수로 래핑한 형태로 반환 가능하게 함
- actionCreator가 함수를 반환하는데, 이 함수는 dispath와 getState를 파라미터로 갖고 내부에서 비동기적 action을 dispatch 가능

즉 redux-thunk는 객체 대신 함수를 생성하는 액션 생성 함수를 작성할 수 있게 해준다.

**일반적인 dispatch 예시**

```javascript
store dispatch({type: 'DO_SOMETHING' })
```

**Redux-Thunk dispatch 예시**

```javascript
store.dispatch((dispatch, getState) => {
  dispatch({ type: DO_SOMETHING });
});
```

---

## redux-thunk의 특징

- 유용한 함수와 리듀서를 만들어 상태를 관리하면 깔끔하게 기능을 구현할 수 있다.
- redux-thunk는 네트워크 요청과 같은 비동기 작업을 관리하면 매우 유용하다.
- 특정한 조건이 만족되면 디스패치 할 수 있는 기능이 있다.

---

## Promise 란?

Promise는 자바스크립트 비동기 처리에 사용되는 객체

promise 객체는 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타낸다.

Promise는 프로미스가 생성될 때 꼭 알 수 있지는 않은 값을 위한 대리자로, 비동기 연산이 종료된 이후의 결과값이나 실패 이유를 처리하기 위한 처리기를 연결할 수 있도록 한다.

Promise를 사용하면 비동기 메서드에서 마치 동기 메서드처럼 값을 반환할 수 있다.

Promise는 주로 서버에서 받아온 데이터를 화면에 표시할 때 사용한다.

---

## Promise의 3가지 상태(states)

Promise의 처리 과정

new Promise()로 Promise를 생성하고 종료될 때까지 3가지 상태를 갖는다.

1. Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태

2. Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태

3. Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

---

## Promise를 다루는 Redux 모듈을 다룰 때 고려사항

1. Promise가 시작, 성공, 실패했을 때 다른 액션을 디스패치해야한다.

2. 각 Promise마다 thunk 함수를 만들어주어야 한다.

3. 리듀서에서 액션에 따라 로딩 중, 결과, 에러 상태를 변경해주어야 한다.

---
