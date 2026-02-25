import os 
from dotenv import load_dotenv, dotenv_values
from pathlib import Path
from flask import jsonify


def v_l_d_d(nome=None):
    
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
    
    try:
        ark = str(nome) # Essa variavel vai pegar o nome
        path= Path(__file__).resolve().parent / "db"  / "intern" / ark #será o caminho
        
        # print(bool(path))
        rsp = load_dotenv(path)
        
        if bool(rsp) == False:
            # print(f"\n -> {bool(rsp)}\n")
            raise FileNotFoundError 
        else:
            pass
        
        rsp = dotenv_values(path)
        dados = {
                "tp" : rsp['FLASK_ENV_DEV'],
                "ch": rsp['FLASK_SECRET_DEV'],
                "debug": rsp['FLASK_DEBUG_DEV'],
                "port": rsp['PORT_DEV']
            }
        # return dados
        
        
    except FileNotFoundError as error:
        return(f"\n__ arquivo não encontrado ___\n__ Erro: {error} __\n")
    except ModuleNotFoundError as error:
        return (f"\n__ {error}")
    except KeyError as error:
        return (f"__\n A chave {error} não pode ser encontrada __\n")
    else:
        return dados 
    