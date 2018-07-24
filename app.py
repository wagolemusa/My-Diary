from flask import Flask, jsonify, request
from models import *
import psycopg2

app = Flask(__name__)


app.config['SECRET_KEY'] = 'refuge'

dbcon = psycopg2.connect(dbname='mydiary', user='postgres', password='refuge', host='localhost')

dbcur = dbcon.cursor()



@app.route('/')
def home():
	return "Start Now Create Your Diaries"


"""User Register"""
@app.route('/api/v2/auth/signup', methods=['POST'])
def register():
#@dbcon.commit()
	if request.method == 'POST':
		full_name = request.get_json()['full_name']
		username  = request.get_json()['username']
		email     = request.get_json()['email']
		password  = request.get_json()['password']
		dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
		dbcon.commit()
	return jsonify({"message": 'Succefuly Registerd'}), 200

""" User Login"""
@app.route('/api/v2/auth/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'POST':

		username = request.get_json()['username']
		password = request.get_json()['password']
		dbcur = dbcon.cursor()
		result = dbcur.execute("SELECT * FROM users WHERE username = %s", [username])
		#if result > 1:
		data = dbcur.fetchone()
		#password = data['password']
		dbcon.close()

		#else:
	return jsonify({"message": 'Username not found'})
	return jsonify({"message": 'Welcome to my Diary'})

@app.route('/api/v2/entry', methods=['POST'])
def post_entry():
	if request.method == 'POST':
		title = request.get_json()['title']
		dates = request.get_json()['dates']
		entries = request.get_json()['entries']
		dbcur.execute("INSERT INTO entries(title, dates, entries) VALUES(%s, %s, %s )",(title, dates, entries))
		dbcon.commit()
	return jsonify({"message": 'Successfuly Posted Entries'})


@app.route('/api/v2/get_entries', methods=['GET'])
def get_entries():
	dbcur.execute("SELECT * FROM entries")
	entries  = dbcur.fetchall()
	return jsonify(entries)

@app.route('/api/v2/view_an_entry/<int:id>', methods=['GET'])
def view_an_entry(id):
	dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
	entries = dbcur.fetchone()
	return jsonify(entries)


@app.route('/api/v2/update_an_entry/<int:id>', methods=['PUT'])
def update_entry(id):
	#dbcur = dbcon.cursor()
	dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
	entries = dbcur.fetchone()
	if request.method == 'PUT':
		title = request.get_json()['title']
		dates = request.get_json()['dates']
		entries = request.get_json()['entries']

		dbcur.execute("UPDATE entries SET title=%s, dates=%s, entries=%s WHERE id=%s",(title, dates, entries, id))
		dbcon.commit()
	return jsonify({"massege": "Entries Succesfuly Updated"})





if __name__ == '__main__':
	app.run()