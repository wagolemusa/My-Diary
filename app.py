from flask import Flask, jsonify, request
from models import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'refuge'



@app.route('/')
def home():
	return "Start Now Create Your Diaries"



@app.route('/api/v1/auth/signup', methods=['POST'])
def register():
	#dbcon.commit()
	if request.method == 'POST':
		full_name = request.get_json()['full_name']
		username  = request.get_json()['username']
		email     = request.get_json()['email']
		password  = request.get_json()['password']
		dbcur = dbcon.cursor()
		dbcur.execute("INSERT INTO users(full_name, username, email, password) VALUES(%s, %s, %s, %s)",(full_name, username, email, password))
		dbcon.commit()
	return jsonify({"message": 'Succefuly Registerd'})


if __name__ == '__main__':
	app.run()