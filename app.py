from flask import Flask,jsonify,request, make_response
import json

app = Flask(__name__)

Diaries = [
{
	'id':'1',
	'title':'Code python',
	'date':'20/08/2018',
	'entry':'Next week I will start on my python project'
},
{
	'id':'2',
	'title':'Zoom Meeting',
	'date':'21/08/2018',
	'entry':'I will have the Zoom meeting next week'
}
]


Users = []

user = {'user_id' : 1, 'full_name' :'refuge', 'username' : 'wise', 'email' : 'wise@gmail.com', 'password' : 'wise12', 'confirm_password' : 'wise12'}
Users.append(user)

"""Home page"""
@app.route('/')
def home():
	return jsonify({"message":'Welcome To my Diary'})


""" get all users"""
@app.route('/api/v1/get_all_users', methods=['GET'])
def get_all_users():
	return jsonify({'reg': Users})

"""View all Diary entries"""
@app.route('/api/v1/get_entries', methods=['GET'])
def get_entries():
	return jsonify({'dic':Diaries})

"""Get Entry by ID"""
@app.route('/api/V1/view_entry/<id>', methods=['GET'])
def getEntry(id):
	diary = [dics for dics in Diaries if (dics['id'] == id)]
	return jsonify({'dics': diary})

"""post Entry"""
@app.route('/api/v1/post_entry', methods=['POST'])
def postEntry():
	Data = {
	'id': len(Diaries)+ 1,
	'title':request.json['title'],
	'date':request.json['date'],
	'entry':request.json['entry']
	}
	Diaries.append(Data)
	return jsonify(Data)

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