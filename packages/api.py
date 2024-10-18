import os

import pyrebase
from dotenv import load_dotenv


load_dotenv()
config = {
    "apiKey": os.getenv("MY_API_KEY"),
    "authDomain": os.getenv("project"),
    "databaseURL": os.getenv("db"),
    "storageBucket": os.getenv("stock"),
}

firebase = pyrebase.initialize_app(config)

# Exemple d'accès à la base de données
db = firebase.database()