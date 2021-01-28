from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("login2.html")


@app.route('/post', methods=['POST'])
def post():
    userId = request.form['id']
    userPwd = request.form['pwd']
    msg = "%s님이 로그인 되었습니다." % userId
    return msg


if __name__ == "__main__":
    app.run()