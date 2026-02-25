try:
    from pr import *
    from al import *
    from testes import *
except ModuleNotFoundError:
    from .pr import *
    from .al import *
    from .testes import *
else:
    pass