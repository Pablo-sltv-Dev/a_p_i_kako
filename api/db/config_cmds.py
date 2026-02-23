import mysql.connector
from datetime import datetime
from mysql.connector import pooling,Error
from pathlib import Path
import os
from dotenv import load_dotenv

import hashlib


def carregar(text: str) -> str:
    hasg = hashlib.sha256(text.encode('utf-8'))
    return hasg.hexdigest()



class Cnfg: #configações de conexão
    def __init__(self):
        BASE = Path(__file__).resolve().parent / "intern" 
        ENV_PATH = BASE / ".env"
        load_dotenv(ENV_PATH)
        self.config = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'), 
            'port': os.getenv('DB_PORT', 3306),
             'raise_on_warnings': True,
            'autocommit': True
        }
        # print(self.config)
        
        try:
                self.pool = pooling.MySQLConnectionPool(
                    pool_name= "api_pool", #nome da pool(identificação)
                    pool_size= 5, #maximo de 5 conexões simultaneas
                    pool_reset_session=True, # limpa a sessão entree usos

                    **self.config  # suas configurações do mysql
            )
                print("pools de conexões cirados com sucesso")
        except Error as e:
            print(f"Linha: 29\nError ao criar pool de conexões: {e}")
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

    def teste(self):
        if self.config:
            return '''\n___[__| TESTE DE CONEXAO: OK -|__]\n '''
        else:
            raise ValueError('\n___[__| TESTE DE CONEXAO: ERROR |__]\n')
        
# print(Cnfg().teste())

# Instância global
# db_config = Cnfg()
class Cnx(Cnfg):
    def __init__(self):
        super().__init__()
        # print(self.config)
        self.conexao = mysql.connector.connect(**self.config)
    def teste(self):
        if self.conexao:
            return super().teste()
        elif not self.config or self.conexao:
            raise ValueError('\n___[__| TESTE DE CONEXAO: ERROR |__]\n')


# print(Cnx())

class Crsr(Cnx):
    def __init__(self):
        super().__init__()

        self.cursor = self.conexao.cursor(dictionary=True)
        
    def teste(self):
        if self.config and self.conexao and self.cursor:
            return super().teste()
        elif not self.config or self.conexao or self.cursor:
            raise ValueError('\n___[__| TESTE DE CONEXAO: ERROR |__]\n')
        else:
            return "\nCursor: ERROR\n"

# print(Crsr().teste())
   





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
