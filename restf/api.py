from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

# from flask.ext.mysql import MySQL

from routes.User import CreateUser, GetListUser
# from routes.User import GetListUser

app = Flask(__name__)
api = Api(app)


# Register route
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(GetListUser, '/GetListUser')

if __name__ == '__main__':
    app.run(debug=True)