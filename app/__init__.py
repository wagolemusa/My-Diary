from flask import Flask, jsonify, request
from entries.app import diary 
from route import endpoint
from users.routes import users
app = Flask(__name__)
app.config['SECRET_KEY'] = 'refuge'

app.register_blueprint(diary)
app.register_blueprint(endpoint)
app.register_blueprint(users)


#Load the views
#from app import views