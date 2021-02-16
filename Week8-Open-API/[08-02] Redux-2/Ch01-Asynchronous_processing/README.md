## 01 Redux로 비동기 처리

---

### Redux 미들웨어

    액션 -> 미들웨어 -> 리듀서 -> 스토어

### Redux 미들웨어란?

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

### Redux 미들웨어 구조

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
