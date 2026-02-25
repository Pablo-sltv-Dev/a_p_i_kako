from flask import jsonify, request
from flask_cors import CORS, cross_origin
try:
    from api import app
    from ..models import L_g
except ModuleNotFoundError as error:
     raise ModuleNotFoundError(f"\n__ Erro de importação __\n__ ModuleNotFoundError: {error} __\n")
else:
     pass



@app.route("/aln/teste")
def rsp():
    return jsonify({"menssage":"A rota aluno foi acessada"})


@app.route("/aln_bjj/vrfcc/", methods=['POST']) # seria o login, verifica a info e faz login
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


