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
		if request.headers.get('X-API-KEY')=='':
			return make_response(("You need to first login"), 201)
		try:
			jwt.decode(request.headers.get('X-API-KEY'), "refuge")
		except:
			return jsonify({"message": 'please login again'})
		return g(*args, **kwargs)
	return decorated 

class Home(Resource):

	def get(self):
			return jsonify({"message": 'Welcome To Home Page'})


""" Get all entries """
class AllEntries(Resource):
	def get(self):
		dbcur.execute("SELECT title, dates, entries FROM  entries")
		data = dbcur.fetchall()
		return jsonify(data)


# class UserEntries(Resource):
# 	def get(self):
# 		dbcur.execute("SELECT user_id, title, dates FROM entries WHERE ")


	"""Post Entries"""
class Entry(Resource):
	@required_user
	def post(self):
		if request.method == 'POST':
			title = request.get_json()['title']
			dates = request.get_json()['dates']
			entries = request.get_json()['entries']
			username = jwt.decode(request.headers.get('X-API-KEY'), 'refuge')['username']

			dbcur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
			user_id = dbcur.fetchone()[0]
			dbcur.execute("""INSERT INTO entries(user_id, title, dates, entries)
										VALUES(%s, %s, %s, %s )""",(user_id, title, dates, entries))
			dbcon.commit()
		return jsonify({"message": 'Successfuly Posted Entries'})



		""" Get all Entries"""
	@required_user
	def get(self):
		username = jwt.decode(request.headers.get('X-API-KEY'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s",(username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'GET':
			dbcur.execute("SELECT * FROM entries WHERE user_id =%s",[user_id])
			data  = dbcur.fetchall()
			data_list = []
			for row in data:
				entry_id = row[0]
				title = row[2]

				dates = row[3]
				entries = row[4]
				data_list.append({"entry_id":entry_id, "title":title, "dates":dates, "entries":entries})

		return jsonify({"data": data_list})
		#return jsonify(data)
 

class EntryId(Resource):
	"""View one entry"""
	@required_user	
	def get(self, entry_id):
		username = jwt.decode(request.headers.get('X-API-KEY'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'GET':	
			dbcur.execute("SELECT * FROM entries WHERE user_id =%s AND ID = %s", [user_id, entry_id])
			data = dbcur.fetchone()
		return jsonify(data)


		"""Update Entries"""
	@required_user	
	def put(self, entry_id):
		username = jwt.decode(request.headers.get('X-API-KEY'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s",(username,))
		user_id = dbcur.fetchone()[0]
		if request.method == 'PUT':
			title = request.get_json()['title']
			dates = request.get_json()['dates']
			entries = request.get_json()['entries']
			dbcur.execute("""UPDATE entries SET title=%s, dates=%s, entries=%s
										WHERE user_id=%s AND ID=%s""",
										(title, dates, entries, user_id, entry_id))
			dbcon.commit()
		return jsonify({"massege": "Entries Successfuly Updated"})



	"""Delete  Entries"""
	@required_user	
	def delete(self, entry_id):
		username = jwt.decode(request.headers.get('X-API-KEY'), 'refuge')['username']
		dbcur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
		user_id = dbcur.fetchone()[0]
		dbcur.execute("""DELETE FROM entries WHERE ID =%s AND user_id =%s""", 
									(entry_id, user_id))
		return jsonify({"message":'Post Deleted'})
