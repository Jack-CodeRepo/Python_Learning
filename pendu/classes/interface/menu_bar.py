
# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from tkinter import filedialog

# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

# fonctions liées au menu
# def create_save_file():
#     path_save_file = tk.filedialog.askdirectory()
#     new_save_file = path_save_file+"/save_file.txt"

#     f = open(new_save_file, "w")
#     f.close()
#     modify_conf("FILES", "save_file", new_save_file)


# def open_save_file(defaut_folder=None, default_file=None):
#     if not defaut_folder:
#         defaut_folder = "C:/"

#     if not default_file:
#         get_save_file = get_config_element("FILES", "save_file")
#         if not get_save_file:
#             selected_file = tk.filedialog.askopenfilename(initialdir=defaut_folder,
#                                                 filetypes=[("fichier texte", "*.txt"),
#                                                             ("tout les fichiers", "*.*")
#                                                 ]
#                                                 )

#         modify_conf("FILES", "save_file", selected_file)

#     return default_file


def quitter():
    exit()




# ==================================================================================================
#   CLASSES
# ==================================================================================================

class class_menu_bar(tk.Menu):
    def __init__(self):
        """
            Gere la barre de menu
        """
        
        tk.Menu.__init__(self)

        menu_Fichier = tk.Menu(self, tearoff=0)
        menu_Fichier.add_command(label="Nouveau (inexistant)")
        # menu_Fichier.add_command(label="Créer une sauvegarde", command=create_save_file)
        # menu_Fichier.add_command(label="Ouvrir sauvegarde", command=open_save_file)
        menu_Fichier.add_separator()
        menu_Fichier.add_command(label="Quitter", command=quitter)

        menu_Help = tk.Menu(self, tearoff=0)
        menu_Help.add_command(label="Documentation (inexistant)")
        menu_Help.add_command(label="Mail au support (inexistant)")

        self.add_cascade(label="Fichier", menu=menu_Fichier)
        self.add_cascade(label="Help", menu=menu_Help)