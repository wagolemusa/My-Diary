from flask import Flask, jsonify, request, make_response, Blueprint
from flask_restful import Resource
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
import hashlib
import base64
from functools import wraps
import datetime
from __init__ import *
from validetion import *


users = Blueprint('users', __name__)
dbcon = psycopg2.connect(dbname='refuges', user='postgres', password='refuge', host='localhost')
dbcur = dbcon.cursor()

def required_user(g):
	@wraps(g)
	def decorated(*args, **kwargs):
		if request.headers.get('x-access-token')=='':
			return make_response(("You need to first login"), 201)
		try:
			jwt.decode(request.headers.get('x-access-token'), "refuge")
		except:
			return jsonify({"message": 'please login again'})
		return g(*args, **kwargs)
	return decorated 

class Users(Resource):
	"""User Register"""
	def post(self):
		if request.method == 'POST':
			full_name = request.get_json()['full_name']
			username = request.get_json()['username']
			email = request.get_json()['email']
			password = request.get_json()['password']
			confirm_password = request.get_json()['confirm_password']
			if password == confirm_password:
				password = sha256_crypt.encrypt(str(request.get_json()['password']))
				x = dbcur.execute("SELECT * FROM users WHERE username = '"+username+"' OR email = '"+email+"';")
				x = dbcur.fetchone()
				if x is not None:
					dbcon.commit()
					return jsonify(({"massege":"The username  or email is already taken"}), 201)
				else:
					dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
					dbcon.commit()
			else:
				return jsonify({"message": 'password do not match'})
		return jsonify({"message": 'Successfully Registered'})

	""" User Login"""
class Login(Resource):
	def post(self):
		if request.method == 'POST':
			username = request.get_json()['username']
			password = hashlib.sha256(base64.b64encode\
				(bytes(request.get_json()['password'], 'utf-8'))).hexdigest()
			
			payload = {}
			dbcur = dbcon.cursor()
			dbcur.execute("SELECT * FROM users WHERE username = %s;", [username])
			data = dbcur.fetchone()
			if data is not None:
				payload = {"username":username, "password":password,\
			 					"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=45)}
				token = jwt.encode(payload, 'refuge')
				return jsonify({"token":token.decode('utf-8')})
			else:
				return jsonify({"message": 'Wrong Credatials'})

class UpdateUser(Resource):
	""" update user"""
	@required_user	
	def put(self, user_id):
		username = jwt.decode(request.headers.get('x-access-token'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s",(username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'PUT':
			full_name = request.get_json()['full_name']
			username = request.get_json()['username']
			email = request.get_json()['email']
		dbcur.execute("""UPDATE users SET full_name=%s, username=%s, email=%s
										WHERE user_id=%s""",
										(full_name, username, email, user_id))
		dbcur.execute("SELECT * FROM users WHERE user_id =%s", [user_id])
		data  = dbcur.fetchall()
		data_user = []
		for row in data:
			user_id = row[0]
			full_name = row[1]
			username = row[2]
			email = row[3]
			data_user.append({"user_id":user_id, "full_name":full_name, "username":username, "email":email})
		return jsonify({"data": data_user})
		dbcon.commit()
		return jsonify({"massege": "User Successfuly Updated"})



""" get all users"""
class All_Users(Resource):
	def get(self):
		dbcur.execute("SELECT user_id, full_name, username, email FROM users")
		data = dbcur.fetchall()
		for user in data:
			user_id = user[0]
			full_name = user[1]
			username = user[2]
			email = user[3]
			Users = ({"user_id":user_id, "full_name":full_name, "username":username, "email":email})
		return jsonify({"data": Users})
		
		

class UserId(Resource):
	""" get user """
	@required_user
	def get(self):
		username = jwt.decode(request.headers.get('x-access-token'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s",(username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'GET':
			dbcur.execute("SELECT * FROM users WHERE user_id =%s",[user_id])
			data  = dbcur.fetchall()
			Users = []
			for u in data:
				user_id = u[0]
				full_name = u[1]
				username = u[2]
				email = u[3]
		
				Users.append({"user_id":user_id, "full_name":full_name, "username":username, "email":email})
		return jsonify({"data": Users})


class UserLogout(Resource):
	@required_user
	def get(self):
		try:
			token = request.headers.get('x-access-token')
			clear = "DELETE FROM blacklist WHERE time < NOW() - INTERVAL '45 minutes';"
			sql = " INSERT INTO blacklist(token)VALUES ('"+token+"');"
			dbcur = dbcon.cursor()
			dbcur.execute(clear)
			dbcur.execute(sql)
			dbcon.commit()
			return jsonify({"message":"You have been successfully logged out. Token invalidate"})
		except TypeError:
			return jsonfy({"message":'You con only logout if you were logged in'})
