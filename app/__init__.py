from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api
from entries.app import Entry
from route import endpoint
from users.routes import users


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Entry, '/v2/entries')


#app.register_blueprint(endpoint)
#app.register_blueprint(users)


#Load the views
#from app import views