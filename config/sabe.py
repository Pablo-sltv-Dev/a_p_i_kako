import hashlib


def carregar(text: str) -> str:
    hasg = hashlib.sha256(text.encode('utf-8'))
    return hasg.hexdigest()


