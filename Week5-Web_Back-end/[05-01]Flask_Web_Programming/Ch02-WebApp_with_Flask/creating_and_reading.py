from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

board = []


@app.route('/')
def index():
    return render_template('Board.html', rows=board)


@app.route('/add', methods=["POST"])
def add():
    if request.method == "POST":
        board.append([request.form['name'], request.form['context']])
        return redirect(url_for('index'))
    else:
        return render_template('Board.html', rows=board)


if __name__ == "__main__":
    app.run(debug=True)
