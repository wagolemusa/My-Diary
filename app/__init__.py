from flask import Flask, jsonify, request, Blueprint
from flask_restful import Api
from flask_cors import CORS

from entries.app import Entry
from entries.app import EntryId
from entries.app import AllEntries
from entries.app import  Home
from entries.app import AllEntries
from entries.app import ShowEntries
from users.routes import Users
from users.routes import Login
from users.routes import UserId
from users.routes import All_Users
from users.routes import UpdateUser
from users.routes import UserLogout




# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)


api_bp = Blueprint('api', __name__)
CORS(api_bp, resources=r'/api/*', headers='Content-Type')
api = Api(api_bp)


api.add_resource(Home, '/')
api.add_resource(Entry, '/v2/entries')
api.add_resource(AllEntries, '/v2/all_entries')
api.add_resource(ShowEntries, '/v2/all_entries/<int:entry_id>')
api.add_resource(Users,  '/v2/auth/signup')
api.add_resource(Login,  '/v2/auth/login')
api.add_resource(UserId,  '/v2/profile')
api.add_resource(All_Users,    '/v2/users')
api.add_resource(UserLogout,   '/v2/users/logout')
api.add_resource(UpdateUser, '/v2/profile/update/<int:user_id>')
api.add_resource(EntryId, '/v2/entries/<int:entry_id>')



