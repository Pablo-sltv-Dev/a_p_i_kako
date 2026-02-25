#bibliotecas:

from flask import Flask
from flask_cors import CORS

#______________________________









app = Flask(__name__)






from .routes import *
from .config import *
from .db import *
from .models import *

@app.before_request
def vrf_point():
    try:
        if not request.endpoint:
            raise ModuleNotFoundError
    except ModuleNotFoundError as error:
        print(f"\n__ Endpoint não encontrado__\n {error}")
        return jsonify({"Menssage": "endpoint não encontrado"})

# except ImportError:
#     from .routes import *
#     from .config import *
#     from .db import *
#     from .models import *

# else:
#     pass

sucess = v_l_d_d()



