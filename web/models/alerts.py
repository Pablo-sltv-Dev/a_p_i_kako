from web import app
from flask import jsonify, request



@app.get("/lrt")
def cnx():
    return jsonify({"status": "online", "conexão": True})