from db import c_M_N_D_s_A_l_N, carregar


class L_g:
    
    def __init__(self, x, y, z):
        self.bnc = c_M_N_D_s_A_l_N()
        self.n_m =  x #nome
        self.d_t = y # data de nascimento
        self.s_h = carregar(z) # senha

    def vrc(self):
        if self.n_m:
            return True
        else:
            False
    def x(self):
        print(self.s_h)
        p = False
        dds = self.bnc.tudo()
        
        for d in dds:
            while True:
                if self.n_m != d['nome'] and self.s_h != d['chave']:
                    p = False
                    break
                elif self.n_m == d['nome'] and self.s_h == d['chave']:
                    print("o login foi")
                    p = True
                    # print(d['nome'])
                    return True
                # return True
                else:
                    p = None
                    pass
        if p == False:        
            return False
        else:
            return None