from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api
from entries.app import Entry
from users.routes import Users
from users.routes import Login

from route import endpoint


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Entry, '/v2/entries')
api.add_resource(Users,  '/v2/auth/signup')
api.add_resource(Login,  '/v2/auth/login')



#app.register_blueprint(endpoint)
#app.register_blueprint(users)


#Load the views
#from app import views