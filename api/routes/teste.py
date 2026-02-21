from api import app
from flask import jsonify

@app.route("/teste")
def home():
    return jsonify({"menssage": "API está funcionando"})