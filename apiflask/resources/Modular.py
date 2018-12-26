from flask_restful import Resource


class Modular(Resource):
    def get(self):
        return {"message": "Hello Modular get!"}

    # example of post request
    def post(self):
        return {"message": "Hello, Modular post!"}