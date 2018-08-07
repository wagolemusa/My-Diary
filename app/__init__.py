from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api
from entries.app import Entry
from entries.app import EntryId
from entries.app import  Home
from users.routes import Users
from users.routes import Login
from users.routes import UserId
from users.routes import UpdateUser


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Home, '/')
api.add_resource(Entry, '/v2/entries')
api.add_resource(Users,  '/v2/auth/signup')
api.add_resource(Login,  '/v2/auth/login')
api.add_resource(UserId,  '/v2/profile')
api.add_resource(UpdateUser, '/v2/profile/update')
api.add_resource(EntryId, '/v2/entries/<int:entry_id>')


