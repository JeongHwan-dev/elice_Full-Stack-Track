from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/get', methods=['GET'])
def get():
    userId = request.args.get('id')
    userPwd = request.args.get('pwd')
    msg = "%s님이 로그인 되었습니다." % userId
    return msg


if __name__ == "__main__":
    app.run()
