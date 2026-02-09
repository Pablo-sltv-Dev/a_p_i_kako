from web import app
from flask import jsonify, request, redirect, url_for
from flask_cors import CORS
import os

from dotenv import load_dotenv

from .mstr import *
from .aln import *
from ..models import *




@app.route("/") # rota 1 
def home():
    return redirect(url_for('cnx'))


@app.route("/lg")
def vsfd():
    dados = request.get_json()
    print(dados)
    if dados:
        vr = L_g(dados['x'], dados['y'], dados['z'])
        if vr.vrc() == False:
            return jsonify({"mensgam": "sem dados"})
        else:
            rsp = vr.x()
            if rsp == dados['x']:    
               return redirect(url_for('aln', nm = rsp))
            elif rsp == False:
               return jsonify({"mensagem": "informacoes invalidas"})
                
            else:
               return jsonify({"mensagem": "Erro no sistema"})
     


# @app.route("/kk_bjj", methods=['POST'])
# def mudar_nome(tp,ds): 
#      if tp == "psqs" and  request.method == 'POST':
#          dados = pr(ds)
#          if dados != None:
#           return jsonify({'Resultado':'positivo',"nome" : dados[0],"numero": dados[1],"dt_nsc": dados[2],"email":dados[3]})
#          elif dados == None:
#           return jsonify({"Resultado": None})
#          else:
#               return jsonify({"mensage": "acheei"})
#      elif tp == "mtrcl" and request.method == 'POST':
#           print("acesso em m_a")
#           nv_aln = ds #pelo oq eu entendi ele vai pegar todos os dados
#           if nv_aln == None or nv_aln == False:
#                print("sem dados")
#                return jsonify({"mensagem": "Sem dados"})
#           else:
#                dados = {
#                          "nome" : nv_aln.get('nome'),
#                          "numero" : nv_aln.get('numero'),
#                          "data de nascimento" : nv_aln.get('dt_nscmnt'),
#                          "email": nv_aln.get('mil'),
#                          "senha" : nv_aln.get('snh')
#                     }
                    
#           if mudar(dados) == True:
#                return jsonify({"mensagem": "cadastro feito com sucesso"})
          
#           else: 
#                return jsonify({"mensage": "erro"})
          
#      elif tp == "exemplo" and request.method == 'POST':
#           print("alguém acessou teste")
#           dado = ds
#           if dado != None:
#                print("Mensagem : Dados recebidos com sucesso")
#                return jsonify({"mensage": "dados recebidos"})
#           else:
#                print("erro ao receber dados")
#                return json({'mensagem': 'Erro'})
#      else:
#          print("erro lnh 61 main")
#          return False
               
                


# @app.get("/aln/<tp>/")
# def aln_opcs(tp, ds):
#     if tp == 'teste':
#         return jsonify({"mesage": "a rota aluno está acessivel", "dados": ds})

    


