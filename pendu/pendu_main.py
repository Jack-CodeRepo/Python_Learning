# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

# import framework GUI tkinter
import tkinter as tk
from tkinter import filedialog

# import module standard python
import configparser
import os
import random

# import dictionnaire
from words import words_list

# import des éléments modifiables
import classes.elements.player
import classes.elements.mot
import classes.elements.lettre

# import des composants d'interface
import classes.interface.menu_bar
import classes.interface.bouton
import classes.interface.saisie
import classes.interface.display

# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

save_file = "save_file.txt"
conf_file = "pendu.conf"

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
    config.read(conf_file)
    config.set(section, option, value)

    with open(conf_file, 'w') as configfile:
        config.write(configfile)


def get_config_element(section, option):
    config = configparser.ConfigParser()
    config.read(conf_file)
    value = config.get(section, option)

    return value



# fonctions liées à l'interface autre que le menu
def add_player(name):
    check_empty_file = os.stat(save_file).st_size == 0
    name = name
    if check_empty_file:
        with open(save_file, 'a') as fichier:
            fichier.write(f"{name}=10")

    if not check_empty_file:
        with open(save_file, 'a') as fichier:
                fichier.write(f"\n{name}=10")


def get_list_players():
    with open(save_file, 'r') as fichier:
        lignes = fichier.readlines()
        joueur = []
        for l in lignes:
            nom_joueur = l.split("=")
            joueur.append(nom_joueur[0])
    return joueur


def get_score_from_save(name):
    with open(save_file, 'r') as fichier:
        lignes = fichier.readlines()
        for l in lignes:
            nom_joueur = l.split("=")[0]
            score = l.split("=")[1]
            if name == nom_joueur:
                return score


def write_player_score(name, score):
    with open(save_file, 'w') as fichier:
        lignes = fichier.readlines()
        nb_lignes = len(lignes)
        for i in nb_lignes:
            index = i
            for l in lignes:
                nom_joueur = l.split("=")[0]
                score = l.split("=")[1]
                if name == nom_joueur:
                    lignes[index] = f"{nom_joueur}={score}"
                    fichier.writelines(lignes)


def hide_word(word):
    mot = []
    mot_long = len(word)
    for i in range(mot_long):
        mot.insert(i, "_ ")
    return mot




def affichage(objet, liste):
    '''
        affiche les éléments
        Arguments:
        objet: objet gérant endroit où afficher (l'objet doit etre créé avec la classe display)
        liste: liste des éléments à afficher

    '''
    if type(liste) is list:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        for l in liste:
            objet.insert('1.0', l)
        objet.config(state=tk.DISABLED)

    else:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        objet.insert('1.0', liste)
        objet.config(state=tk.DISABLED)



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent

        self.player = classes.elements.player.class_player()
        self.mot = classes.elements.mot.class_mot()
        self.mot_cache = classes.elements.mot.class_mot()
        self.lettre = classes.elements.lettre.class_lettre()

        self.label_player = tk.Label(parent)
        self.label_player.grid(row=0, column=1, sticky='nsew')

        self.main_display = classes.interface.display.display(parent, 0, 0, 30, 10, 20).get_text()

        self.select_player_input = classes.interface.saisie.saisie(parent, 1, 1, "nom du joueur")
        self.lettre_input = classes.interface.saisie.saisie(self.parent, 3, 2, "lettre")

        self.pendu_play_button = classes.interface.bouton.bouton(parent, 2, 1, "jouer", self.pendu_game)
        self.lettre_button = classes.interface.bouton.bouton(self.parent, 3, 1, "valider lettre", self.get_letter)


    def pendu_game(self):
        self.check_player()


    def get_letter(self):
        a = self.lettre_input.get_value()
        self.lettre.set_name(a)


    def check_player(self):
        a = self.select_player_input.get_value()
        self.player.set_name(a)
        nom_joueur = self.player.get_name()

        players = get_list_players()

        if a:
            nom_joueur = nom_joueur.upper()
            if players:
                if nom_joueur in players:
                    # si le joueur existe
                    for p in players:
                        if nom_joueur == p:
                            self.player.set_name(nom_joueur)
                            s = get_score_from_save(nom_joueur)
                            self.player.set_score(s)
                            string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                            self.label_player.config(text=string)
                else:
                    # si le joueur n'existe pas
                    self.player.set_name(nom_joueur)
                    self.player.set_score(10)
                    add_player(nom_joueur)
                    string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                    self.label_player.config(text=string)
            # si le fichier de sauvegarde est vide
            else:
                self.player.set_name(nom_joueur)
                self.player.set_score(10)
                add_player(nom_joueur) 
                string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                self.label_player.config(text=string)
        else:
            string = "Renseignez un nom de joueur"
            self.label_player.config(text=string)
            affichage(self.main_display, string)

#
#   TO DO 
#   fonction du pendu
#
#






# ==================================================================================================
#   SCRIPT
# ==================================================================================================
root = tk.Tk()

save_file = get_config_element("FILES", "save_file")
menu = classes.interface.menu_bar.class_menu_bar()


root.title("Jeu du pendu")
root.config(menu=menu)

root.geometry("600x200")

interface_main(root)

root.mainloop()