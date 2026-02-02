from web import app
from ..config import *

@app.get("/aln_bjj/vrfcc/")
def proce(dado):
    if dado != None or dado:
        v = C_m_n_d_S()
        v.c_h_k(dado)
    else:
        return False