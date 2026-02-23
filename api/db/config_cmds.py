import mysql.connector
from datetime import datetime
from mysql.connector import pooling,Error
from pathlib import Path
# import os
from dotenv import load_dotenv, dotenv_values

import hashlib


def carregar(text: str) -> str:
    try:
        if type(text) != str:
            raise TypeError("\n Tipo Inválido \n")
        elif text.strip() == "":
            raise ValueError("\n a variavel está vazia \n")
    except TypeError:
        raise TypeError("\n Tipo Inválido \n")
    except ValueError:
        raise ValueError("\n a variavel está vazia \n")
    else:
        hasg = hashlib.sha256(text.encode('utf-8'))
        return hasg.hexdigest()



class Cnfg: #configações de conexão
    def __init__(self):
        try:
            BASE = Path(__file__).resolve().parent / "intern" 
            ENV_PATH = BASE / ".env"
            carregado = load_dotenv(ENV_PATH)
            
            if not BASE.exists(): #verifica se a pasta existe
                raise FileNotFoundError
            if not ENV_PATH.exists(): #verifica se o arquivo existe
                raise FileNotFoundError
            if not carregado:
                raise RuntimeError
            
        except FileNotFoundError as error:
            print(f"\n__Pasta ou arquivo inexistente__\n{error}\n")
        except RuntimeError:
            print("\n__erro ao executar arquivo__\n")    
        else:
            
                try:
                    carregado = dotenv_values(ENV_PATH)
                
                    self.config = {
                        'user': carregado['DB_USER'],
                        'password': carregado['DB_PASSWORD'],
                        'host': carregado['DB_HOST'],
                        'database': carregado['DB_NAME'], 
                        'port': carregado['DB_PORT'],
                        'raise_on_warnings': True,
                        'autocommit': True
                        }
                
                except KeyError as error:
                    print(f"\n__Chave Inexistente__{error}\n")
                
                # if not self.config['user'].exists():
                #     raise KeyError
            
            

            
            # print("ok")
        
        try:
                self.pool = pooling.MySQLConnectionPool(
                    pool_name= "api_pool", #nome da pool(identificação)
                    pool_size= 5, # maximo de 5 conexões simultaneas
                    pool_reset_session=True, # limpa a sessão entree usos

                    **self.config  # suas configurações do mysql
            )
                # print("pools de conexões cirados com sucesso")
        except Error as e:
            # print(f"Linha: 29\nError ao criar pool de conexões: {e}")
            self.pool = None
    
            
   
            
          

    def get_connection(self):
        """Retorna uma conexão do pool"""
        try:
            return self.pool.get_connection()
        except Error as e:
            print(f"Linha:37\n❌ Erro ao obter conexão: {e}")
            return None

    def test_connection(self):
        """Testa a conexão com o banco"""
        try:
            connection = self.get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                cursor.close()
                connection.close()
                return True, "Conexão bem-sucedida!"
        except Error as e:
            return False, f"Erro na conexão: {e}"
        return False, "Falha na conexão"

 
        
# print(Cnfg())


class Cnx(Cnfg):
    def __init__(self):
        super().__init__()
        try: 
        # print(self.config)
            self.conexao = mysql.connector.connect(**self.config)
            if not self.conexao:
                raise AttributeError
            
        except AttributeError as error:
            print(f"\n__Configuração não definida___\n {error}\n")
        except ValueError as error:
            print(f"Error no {error}")


    


# print(Cnx())

class Crsr(Cnx):
    def __init__(self):
        super().__init__()

        try:

            self.cursor = self.conexao.cursor(dictionary=True)
            if not self.cursor:
                raise TypeError
        except AttributeError as error:
            print(f"\n__variavel inexistente__\n__ {error}__\n")
   


    

# print(Crsr())
   





class c_M_N_D_s_A_l_N(Crsr):
    def __init__(self):
        super().__init__()
    def teste(self):
        return super().teste()

    def tudo(self):
        cmd = " select nome, dt_nscmnt as data, snh as chave from ALUNOS; "
        self.c_r_s_r.execute(cmd)
        dds = self.c_r_s_r.fetchall()
        
                    
       
        # nome data chave
        self.c_r_s_r.close()
        self.c_n_x.close()
        return dds




    def cnvrt(self, t):
        return datetime.strptime(t, '%Y, %m, %d').date()




    def pgr(self):
        self.cursor.execute(" select nome as t, dt_nscmnt as n, snh as k  from ALUNOS ")
        lote = self.cursor.fetchone()[0]
        self.cursor.close()
        self.conexao.close()
        return lote
    

        

# print(c_M_N_D_s_A_l_N().tudo())
