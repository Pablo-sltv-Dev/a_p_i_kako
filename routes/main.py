from web import app
from flask import Flask, jsonify, request
from flask_cors import CORS
from ..config.database import *
import os

from dotenv import load_dotenv





#__isso permite a conexão dos apps


@app.route("/") # rota 1 
def home():
    print("alguem acessou a rota 1")
    # return True
    return jsonify({"message": "API FUNCIONANDO","status": "online"})




