#  TESTES

from api import app
from db import C_m_n_d_S
from .models import L_g
from flask import jsonify, request
from flask_cors import CORS, cross_origin
 
@app.route("/")
def home():
    return jsonify({"ok": True})

#------------------------------------------------------------------------------

# Professor


@app.route("/professor/teste") # edde end testa se a conexão está ok
@cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-b0ccb565-2a2a-4ebc-8f37-9b2a2a20bcf2?action=share&creator=47017727', 'https://kako-bjj.vercel.app/app/templates/opc_one/one.html' ], methods=['GET'])
def teste_professor():
    return jsonify({"mensage": "rota professor ok"})


@app.post("/mtrcl/dc") # Essa seria a rota para cadastro
@cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-e8256144-1fa0-43d1-84a4-9af1f799399c?action=share&creator=47017727', 'https://kako-bjj.vercel.app/app/templates/opc_one/one.html'],methods=['POST'], allow_headers=['Content-Type'])
def adc_prfssr():
     dados = request.get_json()
     x = {
          "nome": dados['nome'],
          "numero": dados['numero'],
          "data de nascimento": dados['data de nascimento'],
          "senha": dados['senha']
     }
    #  x = ""
     
     
          # print(x)
          # return True
     novo_info = C_m_n_d_S()
     if novo_info.C_d_S_t_S(nm=x['nome'], nmr=x['numero'], cf=x['data de nascimento'], nh=x['senha']):
          return jsonify({"menssage":"cadastro feito com sucesso"})


     else: 
          return jsonify({"menssage":"cadastro negado"})





#------------------------------------------------------------------------------

# Aluno


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
