# 데이터 반환하기
# Flask 에서는 데이터를 json 파일 형식으로 데이터를 교환한다.
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def json():
    people = [{'name': 'Elice', 'birth-year': 2015},
              {'name': 'Dodo', 'birth-year': 2016},
              {'name': 'Queen', 'birth-year': 2017}]
    return jsonify(people)      # jsonify() 메소드를 사용해서 데이터를 json 형식으로 바꾼다.


if __name__ == "__main__":
    app.run()