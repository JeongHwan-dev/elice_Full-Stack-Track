var fruits = ["apple", "orange", "cherry"];

// 일반 for문 사용하여 반복
for (var i = 0; i < 3; i++) {
    document.write(i + ": " + fruits[i] + "<br>");
}

document.write("<hr>");

// forEach() 함수를 사용
function myFunction(item, index) {
    document.write(index + ": " + item + "<br>");
}

fruits.forEach(myFunction);