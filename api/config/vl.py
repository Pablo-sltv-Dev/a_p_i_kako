import os 
from dotenv import load_dotenv, dotenv_values
from pathlib import Path
from flask import jsonify


def v_l_d_d(nome=None):
    # BAse_dir =
    if nome == None:
        dados = {
            "tp" : str("production"),
            "ch": None,
            "debug": False,
            "port": 8000
        }
        return dados
    else:
        pass
    # print("ele entendeu que é pra continuar")

    ark = str(nome)
    path= Path(__file__).resolve().parent / "db" / "intern" /ark
    rsp = load_dotenv(path)

    if rsp:
        rsp = dotenv_values(path)
        dados = {
            "tp" : rsp['FLASK_ENV_DEV'],
            "ch": rsp['FLASK_SECRET_DEV'],
            "debug": rsp['FLASK_DEBUG_DEV'],
            "port": rsp['PORT_DEV']
        }
        return dados
    else:
        return "\nerror\n"
    
# print(v_l_d_d(".env"))