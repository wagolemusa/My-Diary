from flask import Flask, jsonify, request

import models

#Intitialize the app
app = Flask(__name__)

#Load the views
from app import views