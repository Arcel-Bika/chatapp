"""
Code de l'API
Discription:
-----------
Ce code est une API qui permet de communiquer avec une base de données Firebase.
Il est possible de lire, écrire, mettre à jour et supprimer des données.
"""

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


# Lire les données
def read_data():
    data = db.child("chat").get()
    return data.val()


def read_data_by_id(id):
    data = db.child("chat").child(id).get()
    return data.val()


# Ecrire des données
def write_data(data):
    db.child("chat").push(data)


# Mettre à jour des données
def update_data(id, data):
    db.child("chat").child(id).update(data)


# Supprimer des données
def delete_data(id):
    db.child("chat").child(id).remove()


# Exemple d'utilisation
if __name__ == "__main__":
    # Lire les données
    data = read_data()
    print(data)

    # Ecrire des données
    write_data({"message": "Hello World"})

    # Mettre à jour des données
    update_data("-Mk7Xw5X5v4Lw8", {"message": "Hello World 2"})

    # Supprimer des données
    delete_data("-Mk7Xw5X5v4Lw8")