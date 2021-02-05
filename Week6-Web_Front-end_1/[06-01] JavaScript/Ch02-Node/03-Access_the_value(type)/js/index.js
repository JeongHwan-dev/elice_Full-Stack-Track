// 1. 아이디가 apple 인 요소의 첫 번째 자식 노드를 선택하도록 코드를 작성하세요.
var apple_node = document.getElementById("apple").childNodes[0];

// 2. apple_node 의 값을 변수에 할당하도록 코드를 작성하세요.
var apple_node_value = apple_node.nodeValue;

// 3. apple_node 의 타입을 변수에 할당하도록 코드를 작성하세요.
var apple_node_type = apple_node.nodeType;

document.write(apple_node_value + "<br>");
document.write(apple_node_type);
