from api import app, C_m_n_d_S
from flask import jsonify, request


from flask import jsonify

from flask_cors import CORS, cross_origin

cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-b0ccb565-2a2a-4ebc-8f37-9b2a2a20bcf2?action=share&creator=47017727', 'https://kako-bjj.vercel.app/'], methods=['GET'])
@app.route("/professor/teste") # edde end testa se a conexão está ok
def teste_professor():
    return jsonify({"mensage": "rota professor ok"})

# from api import *
cross_origin(origins=['https://solotv-3391511.postman.co/workspace/k_a_k_o~a7a0cb57-724d-46a8-a92b-1f33c5fc4836/request/47017727-e8256144-1fa0-43d1-84a4-9af1f799399c?action=share&creator=47017727', 'https://kako-bjj.vercel.app/'], methods=['POST'])
@app.post("/mtrcl/dc") # Essa seria a rota para cadastro
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
    

# @app.post("/professor/vne")
# def prc(dds):
#     if request.method == 'POST':
#         dados = request.get_json()
#         print(dados)
        
#         return jsonify({"mensssage": "tipo post", "dados": dados})
#     elif request.method == 'GET':
#         return jsonify({"mensssage": "tipo get"})
#     else:
#         return jsonify({"mensssage": "Error intern"})
        
        
#     if dados:
#         return redirect(url_for('adc_prfssr', ds = dados))
#     else:
#         return jsonify({"mnessage": "erro no envio dos dados"})
#     return


