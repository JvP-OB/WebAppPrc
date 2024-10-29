from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Building the API first

app = Flask(__name__) #Flask application
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #db instance is created
