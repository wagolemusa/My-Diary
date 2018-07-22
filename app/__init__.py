from flask import Flask 

import models

#Intitialize the app
app = Flask(__name__)

#Load the views
from app import views