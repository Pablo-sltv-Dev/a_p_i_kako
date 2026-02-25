

from flask import Flask, redirect, url_for
from flask_cors import CORS

#______________________________


from flask import jsonify, request
from flask_cors import CORS, cross_origin
try:
    # from api import app
    from db import C_m_n_d_S
except ModuleNotFoundError as error:
     raise ModuleNotFoundError(f"\n__ Erro de importação __\n__ModuleNotFoundError: {error} __\n")
except ImportError as error:
     raise ModuleNotFoundError(f"\n__ Erro de importação __\n__ModuleNotFoundError: {error} __\n")
else:
     pass









app = Flask(__name__)






from config import *
from db import *
from models import *



sucess = v_l_d_d()

@app.route("/")
@cross_origin(origins="https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-9e48bff6-a9a2-4a80-942f-a0aa160357e5?action=share&creator=47017727", methods=['GET'])
def home():
    return jsonify({"Menssage":"A API está online"})

@app.route("/professor/teste") # edde end testa se a conexão está ok
@cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-b0ccb565-2a2a-4ebc-8f37-9b2a2a20bcf2?action=share&creator=47017727'], methods=['GET'])
def teste_professor():
    return jsonify({"mensage": "rota professor ok"})


# @app.post("/mtrcl/dc") # Essa seria a rota para cadastro
# @cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-e8256144-1fa0-43d1-84a4-9af1f799399c?action=share&creator=47017727'],methods=['POST'], allow_headers=['Content-Type'])
# def adc_prfssr():
#      dados = request.get_json()
#      x = {
#           "nome": dados['nome'],
#           "numero": dados['numero'],
#           "data de nascimento": dados['data de nascimento'],
#           "senha": dados['senha']
#      }
#     #  x = ""
     
     
#           # print(x)
#           # return True
#      novo_info = C_m_n_d_S()
#      if novo_info.C_d_S_t_S(nm=x['nome'], nmr=x['numero'], cf=x['data de nascimento'], nh=x['senha']):
#           return jsonify({"menssage":"cadastro feito com sucesso"})


#      else: 
#           return jsonify({"menssage":"cadastro negado"})




@app.route("/aln/teste")
def rsp():
    return jsonify({"menssage":"A rota aluno foi acessada"})


# @app.route("/aln_bjj/vrfcc/", methods=['POST']) # seria o login, verifica a info e faz login
# def proce():
#     dados = request.get_json()
#     resposta = {
#         "nome": dados['nome'],
#         "dta": dados['dta'],
#         "snh": dados['snh']
#     }
#     print(resposta)
#     nv = L_g(resposta['nome'],resposta['dta'],resposta['snh'])
#     if nv:
#         x = nv.x()
#         if x == True:
#             return jsonify({"mensage":"rota acessada"})
#         else:
#             return jsonify({"mensage":"Erro de login"})
#     else:
#         return jsonify({"mensage":"rota não acessada"})





# if __name__ == '__main__':
    
    
#     if sucess:
#         app.run(
#             host='0.0.0.0',
#             port= sucess['port'],
#             debug=sucess['debug']
#         )
#     else:
#         raise ValueError("\nVerifique suas configurações no arquivo .env\n")
#         # print("Verifique suas configurações no arquivo .env")