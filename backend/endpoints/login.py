from flask_restful import Resource

# testing endpoint
class TestingClass(Resource):
    def get(self):
        data = "testing message"
        return data

