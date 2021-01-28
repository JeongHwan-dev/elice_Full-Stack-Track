# flask 패키지에서 Flask를 임포트
from flask import Flask

# Flask 객체 app을 선언
app = Flask(__name__)       # __name__ 은 코드가 실행되면 해당 모듈명이 대입되는 변수


# route() 를 사용해 웹페이지와 해당 페이지에서 작동할 함수를 매칭시킨다.
@app.route('/')
def hello_elice():
    return "Hello Elice!"


# 모듈명이 main 일 때만 실행하도록 조건문을 추가
if __name__ == "__main__":
    app.run()

