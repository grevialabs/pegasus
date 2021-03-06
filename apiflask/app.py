# API entrypoints

from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Modular import Modular

# api_bp = Blueprint('api', __name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)

# Route
# api.add_resource(Hello, '/hello')
api.add_resource(Hello, '/hello')
api.add_resource(Modular, '/')