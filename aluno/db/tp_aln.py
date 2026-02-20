import mysql.connector
from datetime import datetime
from mysql.connector import pooling,Error
import json
import os
from dotenv import load_dotenv




class CnX(CnfG_ALN):
    def __init__(self):
        super().__init__()
        self.c_n_x = mysql.connector.connect(**self.config)
    # def teste(self):
    #     if self.c_n_x:
    #         self.c_n_x.close()
    #         return "\nsucesso\n"
    #     else:
    #         return "\nerror de criação\n"


# print(CnX().teste())

class CrsR(CnX):
    def __init__(self):
        super().__init__()
        self.c_r_s_r = self.c_n_x.cursor()
    def testee(self):
        if self.c_n_x and self.c_r_s_r:
            self.c_r_s_r.close()    
            self.c_n_x.close()
            return "\n SUCESSO \n"
        else:
            return "\nERRO DE SISTEMA\n"

# print(CrsR().testee())

class c_M_N_D_s_ln_tirarissoaq(CrsR):
    def __init__(self):
        super().__init__()


    def tudo(self):
        cmd = " select nome, dt_nscmnt as data, snh as chave from ALUNOS; "
        self.c_r_s_r.execute(cmd)
        dds = self.c_r_s_r.fetchall()
        
                    
        
        # print(v['nome'])
              
        # nome data chave
        # print(dds)
        # print(len(dds))
            
            
        # nome data chave
        self.c_r_s_r.close()
        self.conexao.close()
        return dds




    def cnvrt(self, t):
        return datetime.strptime(t, '%Y, %m, %d').date()

    #     dds = {
    #     "nome" : dados['x'],
    #     "data" : d ,
    #     "s": dados['z']
    #     }
    #     print(dds["data"])
    #     # print()
    #     # c = datetime.str
    #     cmd = " select exists( select 1 from ALUNOS where nome = %s and dt_nscmnt = %s and snh = %s ); "
    #     self.cursor.execute(cmd,(dds["nome"],dds["data"],dds["s"],))
    #     l = self.cursor.fetchall()[0]
    #     print(l)
    #     # "exists( select 1 from ALUNOS where nome = 'teste' and dt_nscmnt = '1111-11-11' and snh = 'senhafalsa' 
        
    #     if bool(l) == True:
    #         return True
    #     else:
    #         return False



    def pgr(self):
        self.cursor.execute(" select nome as t, dt_nscmnt as n, snh as k  from ALUNOS ")
        lote = self.cursor.fetchone()[0]
        self.cursor.close()
        self.conexao.close()
        return lote
        


# def C_h_c_K( n, d, s):
#     print("acessou a linha 151")
#     dados = {
#         "nome" : n,
#         "data" : d,
#         "s": s
#     }
#     arm = c_M_N_D_s_ln().pgr
#     for info in arm:
#         if dados["nome"] == info['t'] and dados["data"] == info[n] and dados["s"] == info['k']:
#             return True
#         else:
#             return False


# d = c_M_N_D_s_ln()  #{'x' : "teste",  'y' : '1111/11/11',    'z' : 'senhafalsa'}

# print(d.cnvrt('1111/11/11'))

