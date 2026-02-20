from api import *
from flask import jsonify, request

@app.route("/professor/teste")
def teste_professor():
    return jsonify({"mensage": "rota professor ok"})

# from api import *
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
