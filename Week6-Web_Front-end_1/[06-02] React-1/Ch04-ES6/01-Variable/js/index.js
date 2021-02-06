// let은 가변 변수로 재정의 가능하지만 재선언은 불가능
let x = 2;
x = 3;
// const는 불변 변수로 재선언과 재정의 모두 불가능
const y = 2;
// var는 재선언과 재정의 모두 가능
var z = 2;
z = 3;

document.write("x = " + x + "<br>");
document.write("y = " + y + "<br>");
document.write("z = " + z + "<br>");