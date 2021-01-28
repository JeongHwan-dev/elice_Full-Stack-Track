# URL 설계하기
from flask import *

# Flask 인스턴스 생성
app = Flask(__name__)


# 홈 페이지로 이동
@app.route('/')
def home():
    return  "주소창에 /user/admin 과 /admin <br/> /user/student 과 /student 를 입력해보세요."


# 관리자 페이지로 이동
@app.route('/admin')
def admin():
    return "This is Admin Page"


# 학생 페이지로 이동
@app.route('/student')
def student():
    return "This is Student Page"


# Error 페이지로 이동
@app.route('/error')
def error():
    return "Error"


# redirect() 함수는 페이지에 다시 연결한다는 뜻으로 아치 페이지를 새로고침 한 것과 같이 동작한다.
@app.route('/user/<name>')
def user(name):
    # 전달 받은 name 이 'admin' 이라면?
    if name == 'admin':
        return redirect(url_for('admin'))
    # 전달 받은 name 이 'student' 라면?
    if name == 'student':
        return redirect(url_for('student'))
    else:
        return redirect(url_for('error'))


if __name__ == "__main__":
    app.run()
