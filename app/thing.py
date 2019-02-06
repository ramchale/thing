from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self, id):
        return {'status': 'Pending', 'found': True}


api.add_resource(HelloWorld, '/processing-status/<int:id>')

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
