from api import app
from flask import jsonify
@app.route("/professor/teste")
def teste_professor():
    return jsonify({"mensage": "rota professor ok"})


