import customtkinter as ctk
from packages import api

def main():
    app = ctk.CTk()  # Crée l'application Tkinter avec l'apparence "custom"

    # Exemple de widget
    label = ctk.CTkLabel(app, text="Bienvenue dans votre application!")
    label.pack(padx=20, pady=20)

    button = ctk.CTkButton(app, text="Cliquez-moi!")
    button.pack(pady=10)

    app.mainloop()


def fetch_data():
    data = api.db.child("votre_noeud").get()  # Exemple de récupération de données depuis la base
    print(data.val())

# Par exemple, ajouter un bouton pour récupérer les données
button = ctk.CTkButton(api.app, text="Récupérer Données", command=fetch_data)
button.pack(pady=10)


if __name__ == "__main__":
    main()
