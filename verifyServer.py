from flask import Flask
from flask_restful import Resource, Api, reqparse
from hashGenerator import HashGenerator
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)

class Verify(Resource):

    def __init__(self):
        self._hashGen = HashGenerator()

    @cross_origin()
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('hash', required=True)  # add args
        parser.add_argument('path', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        latest_hash_val = self._hashGen.get_hash('/Users/animesh.kumar/hackathon/'+args['path'])

        if latest_hash_val != args['hash'] :
            return {
                'message' : "Alert! The backup is tampered with."
            }, 200
        else:
            return {'message' : "backup is safe!"},200
        # read our CSV
api.add_resource(Verify, '/verify')

if __name__ == '__main__':
    app.run()  # run our Flask app