from flask import Flask

app = Flask(__name__)


# / 를 index() 함수와 매칭
@app.route('/')
def index():
    return "Index Page"


# /hello 를 hello() 함수와 매칭
@app.route('/hello')
def hello():
    return "Hello Elice!"


if __name__ == "__main__":
    app.run()
