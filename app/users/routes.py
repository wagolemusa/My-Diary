from flask import Flask, jsonify, request, make_response, Blueprint
from flask_restful import Resource
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
from functools import wraps
import datetime
from __init__ import *


users = Blueprint('users', __name__)
dbcon = psycopg2.connect(dbname='mydiary', user='postgres', password='refuge', host='localhost')
dbcur = dbcon.cursor()


class Users(Resource):
	"""User Register"""
	def post(self):
		if request.method == 'POST':
			full_name = request.get_json()['full_name']
			username  = request.get_json()['username']
			email     = request.get_json()['email']
			password  = request.get_json()['password']
			dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
			dbcon.commit()
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
			#return jsonify({"message": sha256_crypt.verify(password, data[4])})
			if data is not None:
				token = jwt.encode({"username":username, "password":password, "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},'refuge')
				return jsonify({"token":token.decode('utf-8')})
			return jsonify({"message":'Invaild Credentials'})
		return jsonify("Method not allowed")
		