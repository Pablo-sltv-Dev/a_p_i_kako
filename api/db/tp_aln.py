from .config import *
import mysql.connector
from datetime import datetime
# from mysql.connector import pooling,Error

# from dotenv import load_dotenv


import hashlib


def carregar(text: str) -> str:
    hasg = hashlib.sha256(text.encode('utf-8'))
    return hasg.hexdigest()





class CnX(CnfG_ALN):
    def __init__(self):
        super().__init__()
        self.c_n_x = mysql.connector.connect(**self.config)
    def teste(self):
        return super().teste()
    


# print(CnX().teste())

class CrsR(CnX):
    def __init__(self):
        super().__init__()
        self.c_r_s_r = self.c_n_x.cursor(dictionary=True)
    def teste(self):
        return super().teste()

# print(CrsR().teste())

class c_M_N_D_s_A_l_N(CrsR):
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
