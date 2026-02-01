import os
from dotenv import load_dotenv

class config:
    def __init__(self):
        self.url = os.getenv('DATABASE')