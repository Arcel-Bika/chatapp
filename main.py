import customtkinter as ctk
import tkinter as tk
from packages import api  # Import de l'API (à ajuster selon les besoins)


# Initialiser la fenêtre principale
def initialize_main_window():
    root_tk = ctk.CTk()
    root_tk.geometry(f"{root_tk.winfo_screenwidth() - 100}x{root_tk.winfo_screenheight() - 100}")
    root_tk.title("ChatApp")
    root_tk.configure(bg='#202022')

    # Configuration de la grille
    root_tk.grid_columnconfigure(0, weight=1)  # Colonne pour la liste de discussions
    root_tk.grid_columnconfigure(1, weight=8)  # Colonne pour la zone de chat
    root_tk.grid_rowconfigure(1, weight=1)  # Ligne pour étendre les cadres verticalement

    return root_tk


# Créer le titre de l'application
def create_title(root):
    label_title = ctk.CTkLabel(
        master=root, text="ChatApp", width=120, height=60, font=("Arial", 30),
        corner_radius=8, text_color="#F1F1F1"
    )
    label_title.grid(column=0, row=0, padx=10, pady=0, columnspan=2)


# Créer le cadre gauche (liste de discussions)
def create_left_frame(root):
    left_frame = ctk.CTkFrame(root, fg_color='black', bg_color='green')
    left_frame.grid(row=1, column=0, sticky='nsew', padx=(5, 5), pady=5)
    add_discussion_buttons(left_frame)
    return left_frame


# Ajouter des boutons de discussion dynamiquement
def add_discussion_buttons(frame):
    for i in range(9):
        button = ctk.CTkButton(
            master=frame, text=f"Discussion {i + 1}", width=240, height=50,
            corner_radius=5, fg_color="#202022", text_color="#F1F1F1"
        )
        button.pack(pady=5, padx=5)


# Créer le cadre droit (zone de chat)
def create_right_frame(root):
    right_frame = ctk.CTkFrame(root, bg_color='blue')
    right_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)
    create_chat_area(right_frame)
    return right_frame


# Créer la zone de chat avec la liste de messages et la zone de saisie
def create_chat_area(frame):
    chat_list = tk.Listbox(frame, bg="#282828", fg="white", selectbackground="#333333", activestyle="none")
    chat_list.insert(0, "Salut")
    chat_list.insert(1, "Comment tu vas ?")
    chat_list.pack(fill="both", expand=True, padx=5, pady=(5, 0))

    message_var = tk.StringVar()
    message_entry = tk.Entry(frame, textvariable=message_var, bg="#333333", fg="white")
    message_entry.pack(fill="x", padx=5, pady=5)

    send_button = ctk.CTkButton(frame, text="Envoyer", command=None)  # Remplacer `command` par la fonction d'envoi
    send_button.pack(fill="x", padx=5, pady=5)


# Fonction principale pour lancer l'application
def main():
    root_tk = initialize_main_window()
    create_title(root_tk)
    create_left_frame(root_tk)
    create_right_frame(root_tk)
    root_tk.mainloop()


# Lancer l'application
if __name__ == "__main__":
    main()
