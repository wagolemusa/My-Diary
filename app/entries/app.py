from flask import Flask, jsonify, request, Blueprint
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
from functools import wraps
import datetime
from __init__ import *


diary = Blueprint('diary', __name__)

dbcon = psycopg2.connect(dbname='mydiary', user='postgres', password='refuge', host='localhost')
dbcur = dbcon.cursor()

def required_user(g):
	@wraps(g)
	def decorated(*args, **kwargs):
		if request.args.get('token')=='':
			return jsonify({"message": 'You need to first login'})
		try:
			data=jwt.decode(request.args.get('token'), app.config['SECRET_KEY'])
		except:
			return jsonify({"Alert": 'please login again'})
		return g(*args, **kwargs)
	return decorated	

"""Post Entries"""
@diary.route('/api/v2/entries', methods=['POST'])
#@required_user
def post_entry():
	if request.method == 'POST':
		title = request.get_json()['title']
		dates = request.get_json()['dates']
		entries = request.get_json()['entries']
		dbcur.execute("INSERT INTO entries(title, dates, entries) VALUES(%s, %s, %s )",(title, dates, entries))
		dbcon.commit()
	return jsonify({"message": 'Successfuly Posted Entries'})

""" Get all Entries"""
@diary.route('/api/v2/entries', methods=['GET'])
def get_entries():
	dbcur.execute("SELECT * FROM entries")
	data  = dbcur.fetchall()
	return jsonify(data)

"""View one entry"""
@diary.route('/api/v2/entries/<int:id>', methods=['GET'])
def view_an_entry(id):
	dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
	data = dbcur.fetchone()
	return jsonify(data)

"""Update Entries"""
@diary.route('/api/v2/entries/<int:id>', methods=['PUT'])
def update_entry(id):
	dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
	entries = dbcur.fetchone()
	if request.method == 'PUT':
		title = request.get_json()['title']
		dates = request.get_json()['dates']
		entries = request.get_json()['entries']
		dbcur.execute("UPDATE entries SET title=%s, dates=%s, entries=%s WHERE id=%s",(title, dates, entries, id))
		dbcon.commit()
	return jsonify({"massege": "Entries Successfuly Updated"})

