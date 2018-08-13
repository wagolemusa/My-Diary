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
			 					"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)}
				token = jwt.encode(payload, 'refuge')
				return jsonify({"token":token.decode('utf-8')})
			else:
				return jsonify({"message": 'Wrong Credatials'})

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
