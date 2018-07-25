from flask import Flask, jsonify, request
from entries.app import diary 
from route import endpoint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'refuge'
app.register_blueprint(diary)
app.register_blueprint(endpoint)


#Load the views
#from app import views