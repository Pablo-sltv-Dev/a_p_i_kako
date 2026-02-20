from api import app
from flask import jsonify

@app.route("/")
def home():
    return jsonify({"menssage": "API está funcionando"})