from web import app
from flask import jsonify, request
from flask_cors import CORS
from ..config.database import *
import os

from dotenv import load_dotenv

from .mstr import *



#__isso permite a conexão dos apps


@app.route("/") # rota 1 
def home():
    print("alguem acessou a rota 1")
    # return True
    return jsonify({"message": "API FUNCIONANDO","status": "online"})

@app.route('/<tipo>', methods=['POST', 'GET'])
def proces(tipo):
    if tipo == "psqs" and  request.method == 'POST':
        pdd_baby = request.get_json()
        if pdd_baby != None:
               #  print(f"\ninformação captada\n{pdd_baby}\n")
                rspst_daddy = pr(pdd_baby)
                if rspst_daddy:
                     return jsonify({"nome" : rspst_daddy[0],"numero": rspst_daddy[1],"dt_nsc": rspst_daddy[2],"email":rspst_daddy[3]}    
                     )
                if rspst_daddy == None:
                    return jsonify({"mensage": "sem resultados"})
                else:
                     return jsonify({"mensage": "acheei"})
        else:
             return jsonify({"mensage": "sem dados"}) 
    elif tipo == "mtrcl" and request.method == 'POST':

     
        print("acesso em m_a")
        if not request:
             return jsonify({"Mensage": "ERROR", "Tipo":"SEM DADOS"})
        else:
             print("está recebendo")
        nv_aln = request.get_json() #pelo oq eu entendi ele vai pegar todos os dados
        if nv_aln == None or nv_aln == False:
            print("sem dados")
            return jsonify({"mensagem": "Sem dados"})
        else:
            dados = {
                 "nome" : nv_aln.get('nome'),
                 "numero" : nv_aln.get('numero'),
                 "data de nascimento" : nv_aln.get('dt_nscmnt'),
                 "email": nv_aln.get('mil'),
                 "senha" : nv_aln.get('snh')
            }
          
            if mudar(dados) == True:
                 return jsonify({"mensagem": "cadastro feito com sucesso"})
            else: 
                 return jsonify({"mensage": "erro"})
            
          
           




    elif tipo == "exemplo" and request.method == 'POST':
         print("alguém acessou teste")
         dado = request.get_json()
         if dado != None:
              print("Mensagem : Dados recebidos com sucesso")
              return jsonify({"mensage": "dados recebidos"})
         else:
              print("erro ao receber dados")
              return json({'mensagem': 'Erro'})    
    else:
         return jsonify({"mensage": "Error", "Tipo": "identificação inexiste"})        



