from web import app
from flask import Flask, jsonify, request
from flask_cors import CORS
from ..config.database import *
import os

from dotenv import load_dotenv




@app.route('/<tipo>', methods=['POST', 'GET'])
def proces(tipo):
    if tipo == "psqs" and  request.method == 'POST':
        pdd_baby = request.get_json()
        if pdd_baby != None:
                print(f"\ninformação captada\n{pdd_baby}\n")
                return jsonify({"mensagem": "pedido recebido"})
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
            
            nome = nv_aln.get('nome')
            nu = nv_aln.get('numero')
            dt = nv_aln.get('dt_nscmnt')
            m = nv_aln.get('mil', '')
            s = nv_aln.get('snh')
            if not nome  or not nu or not dt  or not  s:
                    return jsonify({"error": "ITENS OBRIGATÓRIOS NAO OBTIDOS"})
            else:
                    novo_info = C_m_n_d_S()
                    
                    if novo_info.C_d_S_t_S(nm=nome, nmr=nu, cf=dt,ml=m, nh=s):
                        print("cadastro feito com sucesso")
                        return jsonify({"mensagem": "cadastro feito com sucesso"})
                    else: 
                        return jsonify({"mensagem": "Erro ao cadastrar "})
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




        




