import pyrebase

config = {
    "apiKey": "VOTRE_API_KEY",
    "authDomain": "VOTRE_PROJET.firebaseapp.com",
    "databaseURL": "https://VOTRE_PROJET.firebaseio.com",
    "storageBucket": "VOTRE_PROJET.appspot.com",
}

firebase = pyrebase.initialize_app(config)

# Exemple d'accès à la base de données
db = firebase.database()
