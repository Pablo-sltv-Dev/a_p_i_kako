import mysql.connector

from mysql.connector import pooling,Error
import json
import os
from dotenv import load_dotenv

import hashlib


def carregar(text: str) -> str:
    hasg = hashlib.sha256(text.encode('utf-8'))
    return hasg.hexdigest()




load_dotenv()

class Cnfg:
    def __init__(self):
        self.config = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'), 
            'port': os.getenv('DB_PORT', 3306),
             'raise_on_warnings': True,
            'autocommit': True
        }
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
            return '''\n___[__| TESTE DE CONEXAO: ERROR |__]\n'''

# Instância global
db_config = Cnfg()








    
        

class Cnx(Cnfg):
    def __init__(self):
        super().__init__()
        self.conexao = mysql.connector.connect(**self.config)

    def teste(self):
        if self.conexao:
            self.conexao.close()
             
            return super().teste()
        else:
            return "\nConexão:ERROR\n"

class Crsr(Cnx):
    def __init__(self):
        super().__init__()

        self.cursor = self.conexao.cursor()
    def teste(self):
        if self.cursor:
            return super().teste()
        else:
            return "\nCursor: ERROR\n"


class C_m_n_d_S(Crsr):
    def __init__(self):
        super().__init__()
    
    
    def v_z_l_z_r(self, pdd):
        cmd = "select nome, nmr, dt_nscmnt, ml from ALUNOS where nome = %s"
        self.cursor.execute(cmd, (pdd,))
        resultado = self.cursor.fetchall()
        d = resultado[0]
        self.cursor.close()
        self.conexao.close()
        return d
        
    def C_d_S_t_S(self, nm, nmr, cf, ml, nh):
        # passe = carregar(nh)
        # -- nome, numero, cpf, email, senha

        novo_cdstr = {"nome" : nm, "numero": nmr, "dtns" : cf,"email": ml,"senha": carregar(nh)}
        
        cmd ="insert into ALUNOS(nome, nmr, dt_nscmnt, ml, snh) value(%s, %s, %s, %s, %s)" #mysql.connector.errors.ProgrammingError: 1064 (42000):

        # cmd = f"insert into ALUNOS(nome,nmr, cpf, ml, snh) value('%{novo_dado["nome"]}', '%{novo_dado['numero']}', '%{novo_dado['cpf']}', '%{novo_dado['email']}', '{novo_dado['senha']}')"
        # self.cursor.execute(cmd,(novo_dado["nome"], novo_dado["numero"], novo_dado["cpf"],novo_dado["email"], novo_dado["senha"]))
        self.cursor.execute(cmd,(novo_cdstr["nome"], novo_cdstr["numero"], novo_cdstr['dtns'] ,novo_cdstr["email"], novo_cdstr["senha"]))
        
        self.cursor.close
        self.conexao.close
        return True
        
    def teste(self, nm, nmr, cf, ml, nh):
        print(nm, nmr, cf, ml, nh)
        return True
    


# print(C_m_n_d_S().v_z_l_z_r("kako"))