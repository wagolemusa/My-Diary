from flask import Flask,jsonify,request, make_response
import json
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'REFUGE'

Diaries = {}

Users = {}

"""Home page"""
@app.route('/')
def home():
	return jsonify({"message":'Welcome To my Diary'})

"""Register User"""
@app.route('/api/v1/auth/regester', methods=['POST'])
def register():

	Register = {request.get_json()['username']:
 {
	'user_id':len(Users) + 1,
	'full_name':request.get_json()['full_name'],
	'email': request.get_json()['email'],
	'password':request.get_json()['password'],
	'confirm_password':request.get_json()['confirm_password']
	}}
	Users.update(Register)
	return jsonify(Users)


"""Login user"""
@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
	username = request.get_json()['username']
	password = request.get_json()['password']
	if username in Users:
		if password == Users[username]['password']:
			token = jwt.encode({"username":username, "password":password, "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])
			return jsonify({"token":token.decode('utf-8')})
		else:
			return jsonify({"message":"Invalid credentials"})
	else:
		return jsonify({"message":"Invalid credentials"})

""" get all users"""
@app.route('/api/v1/get_all_users', methods=['GET'])
def get_all_users():
	return jsonify({'reg': Users})

"""View all Diary entries"""
@app.route('/api/v1/get_entries', methods=['GET'])
def get_entries():
	return jsonify({'dic':Diaries})

"""Get Entry by ID"""
@app.route('/api/V1/view_entry/<int:id>', methods=['GET'])
def getEntry(id):
	return jsonify(Diaries[id])

"""post Entry"""
@app.route('/api/v1/post_entry', methods=['POST'])
def postEntry():
	Data = {
	len(Diaries)+ 1:{
	'title':request.get_json()['title'],
	'date':request.get_json()['date'],
	'entry':request.get_json()['entry']
	}}
	Diaries.update(Data)
	return jsonify(Diaries)

"""Update An Entry"""
@app.route('/api/v1/update_entry/<id>', methods=['PUT'])
def update_entry(id):
	upd = [dics for dics in Diaries if (dics['id'] == id)]
	if 'title' in request.json:
		upd[0]['title'] = request.json['title']
	if 'date' in request.json:
		upd[0]['date'] = request.json['date']
	if 'entry' in request.json:
		upd[0]['entry'] = request.json['entry']
	return jsonify({'dics':upd[0]})



if __name__ =='__main__':
	app.run(debug=True)