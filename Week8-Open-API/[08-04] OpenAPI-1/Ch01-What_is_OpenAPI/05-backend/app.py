from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloElice(Resource):
    def get(self):
        msg = {"message": "Hello Elice"}
        return jsonify(status="success", result=msg)


api.add_resource(HelloElice, '/')

if __name__ == '__main__':
    app.run()
