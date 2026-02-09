from web import app
from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
from ..config.database import *
import os

from dotenv import load_dotenv







# @app.get("/<nome>")
# def pr(nome):
#      print(nome)
#      if nome == None:
#           return None
#      else:
#           daddy = C_m_n_d_S()
#           rsltdd = daddy.v_z_l_z_r(nome)
#           if rsltdd != None:
#                return rsltdd
#           else:
#                return None


        


# @app.post("/mtrcl/dc")
# def mudar(dds):
#      x = dds
#      if x != None:
#           pass
#      else:
#           return False
#      if not x['nome']  or not x['numero'] or not x['data de nascimento']  or not  x['senha']:
#           return jsonify({"error": "ITENS OBRIGATÓRIOS NAO OBTIDOS"})
#      else:
#           # print(x)
#           # return True
#           novo_info = C_m_n_d_S()
#           if novo_info.C_d_S_t_S(nm=x['nome'], nmr=x['numero'], cf=x['data de nascimento'],ml=x['email'], nh=x['senha']):
#                print("cadastro feito com sucesso")
#                return True
               
#           else: 
#                return False


