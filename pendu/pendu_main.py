# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from tkinter import filedialog

import configparser

# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

lol = None
save_file = None
word_dict_file = None


# ==================================================================================================
#   DICT
# ==================================================================================================


# ==================================================================================================
#   LISTS
# ==================================================================================================


# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

def init_config():
    config = configparser.ConfigParser()
    config.read("pendu.conf")
    save_file = config.get("FILES", "save_file")
    word_dict_file = config.get("FILES", "word_dict_file")

    return save_file, word_dict_file


def modify_conf(section, option, value):
    config = configparser.ConfigParser()
    config.read("pendu.conf")
    config.set(section, option, value)

    with open("configuration.conf", 'w') as configfile:
        config.write(configfile)



def create_save_file():
    default_file = tk.filedialog.askdirectory()
    modify_conf("FILES", "save_file", default_file+"/pendu/save.txt")



def open_save_file(defaut_folder=None, default_file=None):
    if not defaut_folder:
        defaut_folder = "C:/"

    if not default_file:
        default_file = save_file
        if not save_file:
            default_file = tk.filedialog.askopenfilename(initialdir=defaut_folder,
                                                filetypes=[("fichier texte", "*.txt"),
                                                            ("tout les fichiers", "*.*")
                                                ]
                                                )
        modify_conf("FILES", "save_file", default_file)

    return default_file

def add_player(save_file, player_name):
    with open(save_file, 'a') as fichier:
        fichier.write(f"{player_name}=10")




def quitter():
    exit()


# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.output = display(parent, 3, 0, 125, 20).get_text()
        self.add_player_affichage = None
        self.add_player = bouton(parent, 0, 0, "Ajouter un joueur", self.cmd_add_player)


    def cmd_add_player(self):
        row = 200
        width = 300
        add_player_window = new_window(self.parent, "Nouveau joueur", row, width)
        self.add_player_affichage = display(add_player_window, 1, 0, row, width).get_text()

        with open(save_file, 'r') as fichier:
            lignes = fichier.readlines()
            joueur = []
            for l in lignes:
                nom_joueur = l.split("=")
                joueur.append(nom_joueur[0])
            self.affichage(self.add_player_affichage,joueur)


    def affichage(self, objet, liste):
        '''
            affiche les éléments
            Arguments:
            objet: objet gérant endroit où afficher (l'objet doit etre créé avec la classe display)
            liste: liste des éléments à afficher

        '''
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        for l in liste:
            objet.insert('1.0', l)
        objet.config(state=tk.DISABLED)




class new_window(tk.Toplevel):
    '''
    '''
    def __init__(self, parent, title, row=200, width=200):
        tk.Toplevel.__init__(self)
        self.title(title)
        self.geometry(f"{width}x{row}")
        self.geometry()


class display(tk.Text):
    '''
        type: class
        Gere la zone d'affichage

        Arguments:
        xRow: coordonnée x (horizontal) de la zone d'affichage
        yCol: coordonnée y (vertical) de la zone d'affichage
        w: largeur de la zone d'affichage
        h: hauteur de la zone d'affichage

    '''
    def __init__(self, parent, xRow, yCol, w, h):
        tk.Text.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.width = w
        self.height = h

        self.boite_texte = tk.Text(parent, width=self.width, height=self.height, state=tk.DISABLED)
        self.boite_texte.grid(row=self.xRow, column=self.yCol, columnspan=3)


    def get_text(self):
        return self.boite_texte



class bouton(tk.Button):
    '''
        type: class
        Gere la zone d'affichage

        Arguments:
        xRow: coordonnée x (horizontal) de la zone d'affichage
        yCol: coordonnée y (vertical) de la zone d'affichage
        titre: nom du bouton
        cmd: fonction à associer au bouton

    '''
    def __init__(self, parent, xRow, yCol, titre, cmd):
        tk.Button.__init__(self)
        self.xRow = xRow
        self.yCol = yCol

        self.bouton = tk.Button(parent, text=titre, height=1, width=15, command=cmd)
        self.bouton.grid(row=self.xRow, column=self.yCol, sticky ="w")



class menu_bar(tk.Menu):
    '''
        type: class
        Gere la barre de menu

        Arguments:
        parent: fenetre parente (main window)

    '''
    def __init__(self, parent):
        tk.Menu.__init__(self)

        menu_Fichier = tk.Menu(self, tearoff=0)
        menu_Fichier.add_command(label="Nouveau")
        menu_Fichier.add_command(label="Créer une sauvegarde", command=create_save_file)
        menu_Fichier.add_command(label="Ouvrir sauvegarde", command=open_save_file)
        menu_Fichier.add_separator()
        menu_Fichier.add_command(label="Quitter", command=quitter)

        menu_Help = tk.Menu(self, tearoff=0)
        menu_Help.add_command(label="Documentation (inexistant)")
        menu_Help.add_command(label="Mail au support (inexistant)")

        self.add_cascade(label="Fichier", menu=menu_Fichier)
        self.add_cascade(label="Help", menu=menu_Help)






# ==================================================================================================
#   SCRIPT
# ==================================================================================================

save_file, word_dict_file = init_config()

root = tk.Tk()
root.title("Jeu du pendu")
root.config(menu=menu_bar(root))

interface_main(root)

root.mainloop()