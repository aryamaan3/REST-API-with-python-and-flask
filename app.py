from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        return "Hello World"


api.add_resource(Test, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True)
