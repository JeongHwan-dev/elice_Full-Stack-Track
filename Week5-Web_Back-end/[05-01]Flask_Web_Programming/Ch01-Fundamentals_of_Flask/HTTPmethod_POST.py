# HTTP 메소드 - POST
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/post', methods=['POST'])
def post():
    name = request.form['input']
    msg = "%s님 환영합니다." % name
    return msg


if __name__ == "__main__":
    app.run()
