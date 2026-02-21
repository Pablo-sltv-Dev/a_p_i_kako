from flask import Flask
from flask_cors import CORS
# from 
from .config import *
from .db import *



app = Flask(__name__)
# from .config import *
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


# CORS(app)
# CORS(app,
#      origins=['http://localhost:0.0.0.5000','https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-9e48bff6-a9a2-4a80-942f-a0aa160357e5?action=share&creator=47017727',
# 'https://kako-bjj.vercel.app/','https://aluno-bjj.vercel.app/'],
#      methods=['GET'],
#      allow_headers=['Content-Type'],
#      supports_credentials=True)

sucess = v_l_d_d('.env')

from .routes import *
from .models import *

from professor import *



