from flask import Flask, jsonify, request
from app import app
from models import *
import datetime

#today = str(datetime.datetime.today())
@app.route('/')
def home():
	return "Start Now Create Your Diaries"



@app.route('/api/v1/auth/signup', methods=['POST'])
def register():
	dbcon.commit()
	if request.method == 'POST':
		full_name = request.get_json()['full_name']
		username  = request.get_json()['username']
		email     = request.get_json()['email']
		password  = request.get_json()['password']
		dbcur = dbcon.cursor()
		dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
		dbcon.close()
	return jsonify({"message": 'Succefuly Registerd'})
