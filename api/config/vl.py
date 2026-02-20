import os 
from dotenv import load_dotenv, dotenv_values
from pathlib import Path
from flask import jsonify


def v_l_d_d(ark: str):
    # BAse_dir =
    path= Path(__file__).resolve().parent / "db" / ark
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
    
# print(v_l_d_d())