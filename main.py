import customtkinter as ctk
import tkinter as tk
from packages import api  # Import de l'API (à ajuster selon les besoins)

# Configuration de la fenêtre principale
root_tk = ctk.CTk()
root_tk.geometry(f"{root_tk.winfo_screenwidth() - 100}x{root_tk.winfo_screenheight() - 100}")
root_tk.title("ChatApp")
root_tk.configure(bg='#202022')  # Couleur de fond de la fenêtre

# Définir les proportions de la grille
root_tk.grid_columnconfigure(0, weight=1)  # Colonne pour la liste de discussions
root_tk.grid_columnconfigure(1, weight=8)  # Colonne pour la zone de chat
root_tk.grid_rowconfigure(1, weight=1)     # Ligne pour que les cadres s'étendent verticalement

# Titre de l'application
label_title = ctk.CTkLabel(
    master=root_tk, text="ChatApp", width=120, height=60, font=("Arial", 30),
    corner_radius=8, text_color="#F1F1F1"
)
label_title.grid(column=0, row=0, padx=10, pady=0, columnspan=2)  # Occuper les deux colonnes pour centrer

# Frame de gauche (Liste de discussions)
left_frame = ctk.CTkFrame(
    root_tk, fg_color='black', bg_color='green'
)
left_frame.grid(row=1, column=0) #sticky='nsew', padx=(5, 5), pady=5

# Frame de droite (Zone de chat)
right_frame = ctk.CTkFrame(
    root_tk, bg_color='blue'
)
right_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)

# Liste des messages dans la zone de chat
chat_list = tk.Listbox(right_frame, bg="#282828", fg="white", selectbackground="#333333", activestyle="none")
chat_list.insert(0, "Salut")
chat_list.insert(1, "Comment tu vas ?")
chat_list.pack(fill="both", expand=True, padx=5, pady=(5, 0))

# Champ de saisie pour envoyer un message
message_var = tk.StringVar()
message_entry = tk.Entry(right_frame, textvariable=message_var, bg="#333333", fg="white")
message_entry.pack(fill="x", padx=5, pady=5)

# Bouton pour envoyer le message
send_button = ctk.CTkButton(right_frame, text="Envoyer", command=None)  # Remplacer `command` par la fonction d'envoi
send_button.pack(fill="x", padx=5, pady=5)

# Fonction pour ajouter des boutons de discussion dynamiquement
def add_discussion_buttons():
    for i in range(9):
        button = ctk.CTkButton(
            master=left_frame, text=f"Discussion {i+1}", width=240, height=50,
            corner_radius=5, fg_color="#202022", text_color="#F1F1F1"
        )
        button.pack(pady=5, padx=5)

# Appel de la fonction pour ajouter les boutons de discussion
add_discussion_buttons()

# Lancement de la boucle principale
root_tk.mainloop()
