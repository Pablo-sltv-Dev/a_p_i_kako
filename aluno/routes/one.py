from api import app, L_g
from flask import jsonify, request

@app.route("/aln_bjj/vrfcc/", methods=['POST'])
def proce():
    dados = request.get_json()
    resposta = {
        "nome": dados['nome'],
        "dta": dados['dta'],
        "snh": dados['snh']
    }
    print(resposta)
    nv = L_g(resposta['nome'],resposta['dta'],resposta['snh'])
    if nv:
        x = nv.x()
        if x == True:
            return jsonify({"mensage":"rota acessada"})
        else:
            return jsonify({"mensage":"Erro de login"})
    else:
        return jsonify({"mensage":"rota não acessada"})
