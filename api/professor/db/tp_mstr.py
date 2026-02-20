from config import *
import mysql.connector
from datetime import datetime
from mysql.connector import pooling,Error

# from dotenv import load_dotenv




# Instância global
# db_config = Cnfg()
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

        self.cursor = self.conexao.cursor(dictionary=True)
        
    def teste(self):
        if self.cursor:
            return super().teste()
        else:
            return "\nCursor: ERROR\n"


class C_m_n_d_S(Crsr):
    def __init__(self):
        super().__init__()
    
    
    
        
        
    def C_d_S_t_S(self, nm, nmr, cf, ml, nh):
        # passe = carregar(nh)
        # -- nome, numero, data de nascimento, senha

        novo_cdstr = {"nome" : nm, "numero": nmr, "dtns" : cf,"email": ml,"senha": carregar(nh)}
        
        cmd ="insert into ALUNOS(nome, nmr, dt_nscmnt, ml, snh) value(%s, %s, %s, %s, %s)" 
        self.cursor.execute(cmd,(novo_cdstr["nome"], novo_cdstr["numero"], novo_cdstr['dtns'] ,novo_cdstr["email"], novo_cdstr["senha"]))
        
        self.cursor.close
        self.conexao.close
        return True
        
    
    def c_h_k(self, dado):
        if dado != None or dado:
            return True
        else:
            return False
    


# class CnfG_ALN:
#     def __init__(self):
#         self.config = {
            
#         }


# class c_M_N_D_s_ln(Crsr):
#     def __init__(self):
#         super().__init__()


#     def tudo(self):
#         cmd = " select nome, dt_nscmnt as data, snh as chave from ALUNOS; "
#         self.cursor.execute(cmd)
#         dds = self.cursor.fetchall()
        
                    
        
        
#         self.cursor.close()
#         self.conexao.close()
#         return dds




#     def cnvrt(self, t):
#         return datetime.strptime(t, '%Y, %m, %d').date()

    

#     def pgr(self):
#         self.cursor.execute(" select nome as t, dt_nscmnt as n, snh as k  from ALUNOS ")
#         lote = self.cursor.fetchone()[0]
#         self.cursor.close()
#         self.conexao.close()
#         return lote
        
    
# # def C_h_c_K( n, d, s):
# #     print("acessou a linha 151")
# #     dados = {
# #         "nome" : n,
# #         "data" : d,
# #         "s": s
# #     }
# #     arm = c_M_N_D_s_ln().pgr
# #     for info in arm:
# #         if dados["nome"] == info['t'] and dados["data"] == info[n] and dados["s"] == info['k']:
# #             return True
# #         else:
# #             return False


# # d = c_M_N_D_s_ln()  #{'x' : "teste",  'y' : '1111/11/11',    'z' : 'senhafalsa'}

# # print(d.cnvrt('1111/11/11'))


# # print(carregar("teste_da_user_0123"))