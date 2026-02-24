try:
    from db import c_M_N_D_s_A_l_N, carregar
except ModuleNotFoundError:
    from .db import c_M_N_D_s_A_l_N, carregar
else:
    pass


class L_g:
    
    def __init__(self, x, y, z):#, y, z):
        self.vld = False
        try:
            resp = self.vr(x, y, z)
            if resp == False:
                raise TypeError
            
        except TypeError as error:
            print(f"\n__ Valor da variavel incorreto __\n__{error}") 
        else:
            self.__bnc = c_M_N_D_s_A_l_N()
            self.n_m =  x #nome
            self.d_t = y # data de nascimento
            self.s_h = carregar(z) # senha
        
    
    def __bool__(self):
        return self.vld
       

       
    def vr(self, one, second, thre):
        # print(f"\n__ {type(one)} __\n")
        try:
            if type(one) != str and type(second) != str and type(thre) != str:
                raise TypeError
        except TypeError as error:
            print(f"\n__ erro no tipo de valor da variavel__\n TypeError: {error} ")
            self.vld = False
        else:
            self.vld = True


    


    
    def x(self):
        # print(self.s_h)
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
        





