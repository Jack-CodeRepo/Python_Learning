# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from tkinter import filedialog

import configparser
import os

from words import words_list

# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

player_name = None

# ==================================================================================================
#   DICT
# ==================================================================================================


# ==================================================================================================
#   LISTS
# ==================================================================================================


# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

# fonctions liées au fichier pendu.conf

def modify_conf(section, option, value):
    config = configparser.ConfigParser()
    config.read("pendu.conf")
    config.set(section, option, value)

    with open("pendu.conf", 'w') as configfile:
        config.write(configfile)


def get_config_element(section, option):
    config = configparser.ConfigParser()
    config.read("pendu.conf")
    value = config.get(section, option)

    return value



# fonctions liées au menu
def create_save_file():
    path_save_file = tk.filedialog.askdirectory()
    new_save_file = path_save_file+"/save_file.txt"

    f = open(new_save_file, "w")
    f.close()
    modify_conf("FILES", "save_file", new_save_file)


def open_save_file(defaut_folder=None, default_file=None):
    if not defaut_folder:
        defaut_folder = "C:/"

    if not default_file:
        get_save_file = get_config_element("FILES", "save_file")
        if not get_save_file:
            selected_file = tk.filedialog.askopenfilename(initialdir=defaut_folder,
                                                filetypes=[("fichier texte", "*.txt"),
                                                            ("tout les fichiers", "*.*")
                                                ]
                                                )

        modify_conf("FILES", "save_file", selected_file)

    return default_file


def quitter():
    exit()





# fonctions liées à l'interface autre que le menu
def add_player(name, file_save):
    check_empty_file = os.stat(file_save).st_size == 0
    if check_empty_file:
        with open(file_save, 'a') as fichier:
            fichier.write(f"{name}=10")
    if not check_empty_file:
        with open(file_save, 'a') as fichier:
            fichier.write(f"\n{name}=10")


def get_list_players(file_save):
    with open(file_save, 'r') as fichier:
        lignes = fichier.readlines()
        joueur = []
        for l in lignes:
            nom_joueur = l.split("=")
            joueur.append(nom_joueur[0])
    return joueur


def get_score_player_name(name, file_save):
    with open(file_save, 'r') as fichier:
        lignes = fichier.readlines()
        for l in lignes:
            nom_joueur = l.split("=")[0]
            score = l.split("=")[1]
            if name == nom_joueur:
                return nom_joueur, score


def get_liste_mots(fichier):
    import words











# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.add_player_input = None
        self.player_name = None
        self.player_score = None
        self.save_file = None

        self.label_player = tk.Label(parent)
        self.main_display = display(parent, 0, 0, 20, 10, 20)
        self.select_player_input = saisie(parent, 1, 2, "nom du joueur")
        self.select_player = bouton(parent, 1, 1, "Valider Joueur", self.manage_player)
        self.pendu_jouer = bouton(parent, 2, 1, "jouer", self.pendu_game)


    def check_save_file(self):
        self.save_file = get_config_element("FILES", "save_file")
        
        if not self.save_file:
            create_save_file()
            self.save_file = get_config_element("FILES", "save_file")

        if not os.path.exists(self.save_file):
            create_save_file()



    def manage_player(self):
        self.check_save_file()
        players_list = get_list_players(self.save_file)
        player_name = self.select_player_input.get_value()
        player_name = player_name.upper()

        if not player_name:
            player_name = "ANONYME"
            add_player(player_name, self.save_file)
            self.player_name = player_name
            string = f"nom du joueur: {self.player_name} // score: 10"
            # self.affichage(self.output, string)
            self.label_player.grid(row=0, column=1, sticky='nsew')
            self.label_player.config(text=string)

        if player_name not in players_list:
            add_player(player_name, self.save_file)
            self.player_name = player_name
            string = str(f"nom du joueur: {self.player_name} // score: 10")
            # self.affichage(self.output, string)
            self.label_player.grid(row=0, column=1, sticky='nsew')
            self.label_player.config(text=string)
        else:
            self.player_name, self.player_score = get_score_player_name(player_name, self.save_file)
            string = str(f"nom du joueur: {self.player_name} // score: {self.player_score}")
            # self.affichage(self.output, string)
            self.label_player.grid(row=0, column=1, sticky='nsew')
            self.label_player.config(text=string)


    def pendu_game(self):
        self.check_save_file()
        if not self.player_name:
            player_name = "ANONYME"
            add_player(player_name, self.save_file)
            self.player_name = player_name
            string = f"nom du joueur: {self.player_name} // score: 10"
            # self.affichage(self.output, string)
            self.label_player.grid(row=0, column=4)
            self.label_player.config(text=string)

        mot_pendu = words_list

        self.affichage(self.main_display, mot_pendu)



    def affichage(self, objet, liste):
        '''
            affiche les éléments
            Arguments:
            objet: objet gérant endroit où afficher (l'objet doit etre créé avec la classe display)
            liste: liste des éléments à afficher

        '''
        if type(liste) != list:
            objet.config(state=tk.NORMAL, font="Calibri")
            objet.delete('1.0', tk.END)
            objet.insert('1.0', liste)
            objet.config(state=tk.DISABLED)
        else:
            objet.config(state=tk.NORMAL, font="Calibri")
            objet.delete('1.0', tk.END)
            for l in liste:
                objet.insert('1.0', l)
            objet.config(state=tk.DISABLED)





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
    def __init__(self, parent, xRow, yCol, w, h, rSpan):
        tk.Text.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.width = w
        self.height = h
        self.rowspan = rSpan

        self.boite_texte = tk.Text(parent, width=self.width, height=self.height, state=tk.DISABLED)
        self.boite_texte.grid(row=self.xRow, column=self.yCol, rowspan=self.rowspan)


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
        self.bouton.grid(row=self.xRow, column=self.yCol, sticky ="nsew")






class saisie(tk.Entry):
    '''
        type: class
        Gere les zone de saisie

        Arguments:
        xRow: coordonnée x (horizontal) de la zone de saisie
        yCol: coordonnée y (vertical) de la zone de saisie
        label: nom de la zone saisie, positionne à gauche de la zone
    '''
    def __init__(self, parent, xRow, yCol, label=None):
        tk.Entry.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.label = label

        # création zone de saisie (entry)
        self.saisie = tk.Entry(parent, width=10)
        self.saisie.grid(row=self.xRow, 
                            column=self.yCol+1
                            )
        # création du nom de la zone de saisie (label)
        self.saisie_label = tk.Label(parent, text=self.label)
        self.saisie_label.grid(row=self.xRow, 
                                column=self.yCol, 
                                sticky="w"
                                )

    def get_value(self):
        '''
            Méthode qui récupere la valeur rentrée
        '''
        return self.saisie.get()







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

root = tk.Tk()
root.title("Jeu du pendu")
root.config(menu=menu_bar(root))
root.geometry("500x200")

interface_main(root)

root.mainloop()