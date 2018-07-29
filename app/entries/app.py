from flask import Flask, jsonify, request, Blueprint,make_response
from flask_restful import Resource
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
from functools import wraps
import datetime
from __init__ import *


diary = Blueprint('diary', __name__)

dbcon = psycopg2.connect(dbname='refuges', user='postgres', password='refuge', host='localhost')
dbcur = dbcon.cursor()

def required_user(g):
	@wraps(g)
	def decorated(*args, **kwargs):
		if request.args.get('token')=='':
			return make_response(("You need to first login"), 201)
		try:
			data=jwt.decode(request.args.get('token'), diary.config['SECRET_KEY'])
		except:
			return ({"Alert": 'please login again'})
		return g(*args, **kwargs)
	return decorated	

class Home(Resource):

	def get(self):
			return jsonify({"message": 'Welcome To Home Page'})

	"""Post Entries"""
class Entry(Resource):
	#@required_user	
	def post(self):
		if request.method == 'POST':
			title = request.get_json()['title']
			dates = request.get_json()['dates']
			entries = request.get_json()['entries']
			username = jwt.decode(request.args.get("token"), "refuge")['username']
			dbcur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
			user_id = dbcur.fetchone()[0]
			dbcur.execute("INSERT INTO entries(user_id, title, dates, entries) VALUES(%s, %s, %s, %s )",(user_id, title, dates, entries))
			dbcon.commit()
		return jsonify({"message": 'Successfuly Posted Entries'})

	
		""" Get all Entries"""
	#@required_user	
	def get(self):
		if request.method == 'GET':
			dbcur.execute("SELECT * FROM entries")
			data  = dbcur.fetchall()
		return jsonify(data)

class EntryId(Resource):

	"""View one entry"""
	#@required_user	
	def get(self, id):
		dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
		data = dbcur.fetchone()
		return jsonify(data)

		"""Update Entries"""
	#@required_user	
	def put(self, id):
		dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
		entries = dbcur.fetchone()
		if request.method == 'PUT':
			title = request.get_json()['title']
			dates = request.get_json()['dates']
			entries = request.get_json()['entries']
			dbcur.execute("UPDATE entries SET title=%s, dates=%s, entries=%s WHERE id=%s",(title, dates, entries, id))
			dbcon.commit()
		return jsonify({"massege": "Entries Successfuly Updated"})

	def delete(self, id):
		dbcur.execute("DELETE FROM entries WHERE id = %s", [id])
		return jsonify({"message":'Post Deleted'})


