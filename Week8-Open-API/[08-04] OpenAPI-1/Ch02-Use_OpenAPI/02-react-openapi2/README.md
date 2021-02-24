## 상품 리스트 출력

저장된 데이터는 딕셔너리로 이루어진 배열형태는 map() 을 활용하여 출력

```javascript
const todoItems = todos.map((todo, index) => <li key={index}>{todo.text}</li>);
```

---
