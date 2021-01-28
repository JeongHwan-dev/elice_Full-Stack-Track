from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form['input']
        return f"{name}님 환영합니다."

    elif request.method == 'GET':
        return render_template('index2.html')

    else:
        msg = "Error"
        return msg


if __name__ == "__main__":
    app.run()
