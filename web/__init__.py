from flask import Flask, jsonify, request
from flask_cors import CORS
from .config.database import *
import os

from dotenv import load_dotenv




load_dotenv()


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


CORS(app)

from .routes import *


