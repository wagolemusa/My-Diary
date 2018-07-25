from flask import Flask, jsonify, request
from models import *
import psycopg2
from passlib.hash import sha256_crypt
import jwt
import datetime
app = Flask(__name__)


app.config['SECRET_KEY'] = 'refuge'

dbcon = psycopg2.connect(dbname='mydiary', user='postgres', password='refuge', host='localhost')

dbcur = dbcon.cursor()



@app.route('/')
def home():
	return jsonify({"message": 'Welcome To Home Page'})


"""User Register"""
@app.route('/api/v2/auth/signup', methods=['POST'])
def register():
	if request.method == 'POST':
		full_name = request.get_json()['full_name']
		username  = request.get_json()['username']
		email     = request.get_json()['email']
		password  = sha256_crypt.encrypt(str(request.get_json()['password']))
		dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
		dbcon.commit()
	return jsonify({"message": 'Succefuly Registerd'}), 200

""" User Login"""
@app.route('/api/v2/auth/login', methods=['GET', 'POST'])
def signin():
	if request.method == 'POST':
		username = request.get_json()['username']
		password = request.get_json()['password']
		dbcur = dbcon.cursor()
		dbcur.execute("SELECT * FROM users WHERE username = %s;", [username])
		data = dbcur.fetchone()
		if data is not None and sha256_crypt.verify(password, data[4]):
			token = jwt.encode({"username":username, "password":password, "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])
			return jsonify({"token":token.decode('utf-8')})
		return jsonify("Invaild Creditaions")
	return jsonify("Method not allowed")

"""Post Entries"""
@app.route('/api/v2/entry', methods=['POST'])
def post_entry():
	if request.method == 'POST':
		title = request.get_json()['title']
		dates = request.get_json()['dates']
		entries = request.get_json()['entries']
		dbcur.execute("INSERT INTO entries(title, dates, entries) VALUES(%s, %s, %s )",(title, dates, entries))
		dbcon.commit()
	return jsonify({"message": 'Successfuly Posted Entries'})

""" Get all Entries"""
@app.route('/api/v2/get_entries', methods=['GET'])
def get_entries():
	dbcur.execute("SELECT * FROM entries")
	entries  = dbcur.fetchall()
	return jsonify(entries)

"""View one entry"""
@app.route('/api/v2/view_an_entry/<int:id>', methods=['GET'])
def view_an_entry(id):
	dbcur.execute("SELECT * FROM 	entries WHERE id = %s", [id])
	entries = dbcur.fetchone()
	return jsonify(entries)

"""Update Entries"""
@app.route('/api/v2/update_an_entry/<int:id>', methods=['PUT'])
def update_entry(id):
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