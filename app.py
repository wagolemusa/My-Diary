from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'refuge'

@app.route('/')
def home():
	return jsonify({"message":'refuge wise'})


if __name__ =='__main__':
	app.run(debug=True)