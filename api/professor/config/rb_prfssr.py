import mysql.connector
from datetime import datetime
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
