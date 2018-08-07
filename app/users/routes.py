from flask import Flask, jsonify, request, make_response, Blueprint
from flask_restful import Resource
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
from functools import wraps
import datetime
from __init__ import *
from validetion import *


users = Blueprint('users', __name__)
dbcon = psycopg2.connect(dbname='refuges', user='postgres', password='refuge', host='localhost')
dbcur = dbcon.cursor()


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
			password = request.get_json()['password']
			dbcur = dbcon.cursor()
			dbcur.execute("SELECT * FROM users WHERE username = %s;", [username])
			data = dbcur.fetchone()
			if data is not None and sha256_crypt.verify(password, data[4]):
				token = jwt.encode({"username":username, "password":password, "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},'refuge')
				return jsonify({"token":token.decode('utf-8')})
			return make_response(("Invaild Credentials"), 201)
		return jsonify("Method not allowed")
		


class UserId(Resource):
	""" get user """
	def get(self):
		username = jwt.decode(request.args.get("token"), "refuge")["username"]
		dbcur.execute("SELECT user_id FROM users WHERE username = %s",(username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'GET':
			dbcur.execute("SELECT full_name, username, email FROM users WHERE user_id =%s",[user_id])
			data  = dbcur.fetchall()
		return jsonify(data)


class UpdateUser(Resource):
	""" Update user """
	def get(self):
		username = jwt.decode(request.args.get("token"), "refuge")["password"]
		dbcur.execute("SELECT * FROM users WHERE password = %s", (password ,))
		data = dbcur.fetchall()
		return jsonify(data)

