from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api
from entries.app import Entry
from entries.app import EntryId
from entries.app import  Home
from users.routes import Users
from users.routes import Login


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Home, '/')
api.add_resource(Entry, '/v2/entries')
api.add_resource(Users,  '/v2/auth/signup')
api.add_resource(Login,  '/v2/auth/login')
api.add_resource(EntryId, '/v2/entries/<int:entry_id>')

