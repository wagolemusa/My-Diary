from flask import Flask, Blueprint, jsonify

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/')
def home():
	return jsonify({"message": 'Welcome To Home Page'})