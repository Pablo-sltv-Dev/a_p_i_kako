from flask import Flask
from flask_cors import CORS
# from 
from .config import *
from .db import *



app = Flask(__name__)


sucess = v_l_d_d(".env")

from .rts import *
from .models import *




# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return {"status": "API viva 🚀"}


