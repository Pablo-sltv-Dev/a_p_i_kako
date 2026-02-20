from api import app
from flask import jsonify
from .db import *
@app.route("/")
def home():
    return jsonify({"menssage": "API está funcionando"})


from professor import *