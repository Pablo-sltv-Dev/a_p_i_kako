from web import app
from ..config import *
from flask import jsonify
@app.route("/<nm>")
def aln(nm):
    if nm == 'kako':
        return jsonify({"mensagem:" : "o usaurio entrou"})
    else:
        return jsonify({"mensagem": "erro de sistema"})