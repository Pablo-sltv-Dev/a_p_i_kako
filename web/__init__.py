from flask import Flask, jsonify, request
from flask_cors import CORS
# from 
from .config.database import *
import os

from dotenv import load_dotenv




load_dotenv()


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


CORS(app)


CORS(app, 
     origins= ['http://127.0.0.1:5500/'],
     methods=['GET', 'POST'],
     allow_headers=['Content-Type', 'Authorization']
     )



from .routes import *


