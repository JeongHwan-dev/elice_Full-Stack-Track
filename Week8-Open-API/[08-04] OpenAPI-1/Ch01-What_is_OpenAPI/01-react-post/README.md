## POST

```javascript
axios.post(url, data 객체)
    .then(function (response) {
        console.log(response);
        console.log(response.data);
        console.log(response.status);
    });
```

---

**response 객체**

반환되는 데이터 (HTTP 상태 코드, 헤더 정보 등)

response.data -> 반환되는 데이터

response.status -> HTTP 상태 코드

---

**POST 시 반환되는 결과를 state인 result에 저장할 때**

```javascript
.then(response => this.setState({ result: 설정할 값 }));
```

---
