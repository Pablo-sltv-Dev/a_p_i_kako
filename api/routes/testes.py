from flask import jsonify #, request
from flask_cors import cross_origin

try:
    from api import app
except ModuleNotFoundError as error:
     raise ModuleNotFoundError(f"\n__ Erro de importação __\n__ ModuleNotFoundError: {error} __\n")
else:
     pass

@app.route("/")
@cross_origin(origins="https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-9e48bff6-a9a2-4a80-942f-a0aa160357e5?action=share&creator=47017727", methods=['GET'])
def home():
    return jsonify({"Menssage":"A API está online"})