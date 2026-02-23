from .db import *

class C_m_n_d_S(Crsr):
    def __init__(self):
        super().__init__()
    
    def teste(self):
        return super().teste()
    
    def V_z_l_z_r(self):
        cmd = "select nome, nmr as numero, dt_nscmnt as data from ALUNOS"
        self.cursor.execute(cmd)
        resposta = self.cursor.fetchall()[0]
        aln = {
            "1.": resposta['nome'],
            "2.": resposta['numero'],
            "3.": resposta['data']
        }
        self.cursor.close()
        self.conexao.close()
        return aln
        
    def C_d_S_t_S(self, nm, nmr, cf, nh):
        # passe = carregar(nh)
        # -- nome, numero, data de nascimento, senha

        novo_cdstr = {
            "nome" : nm, 
            "numero": nmr, 
            "dtns" : cf,
            "senha": carregar(nh)}
        
        cmd ="insert into ALUNOS(nome, nmr, dt_nscmnt, snh) value(%s, %s, %s, %s)" 
        self.cursor.execute(cmd,(novo_cdstr["nome"], novo_cdstr["numero"], novo_cdstr['dtns'] , novo_cdstr["senha"]))
        
        self.cursor.close
        self.conexao.close
        return True
        
    
    def c_h_k(self, dado):
        if dado != None or dado:
            return True
        else:
            return False
 

print(C_m_n_d_S().teste()) 