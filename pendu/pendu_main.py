# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from tkinter import filedialog

import configparser
import os
import random

from words import words_list


# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

player_name = None
save_file = None
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
    name = name.upper()
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


def write_player_score(name, file_save, score):
    with open(file_save, 'w') as fichier:
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


def half_guessed_word(word, lettre, atempt):

    atempt = atempt
    mot = []
    mot_long = len(word)
    word = list(word)
    if lettre in word:
        for i in range(mot_long):
            if word[i] == lettre:
                mot.insert(i, lettre)
            else:
                mot.insert(i, "_ ")
    else:
        atempt -= 1
    return mot, atempt






# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.add_player_input = None

        self.player = joueur()

        self.label_player = tk.Label(parent)
        self.label_player.grid(row=0, column=1, sticky='nsew')
        self.main_display = display(parent, 0, 0, 20, 10, 20).get_text()

        self.select_player_input = saisie(parent, 1, 1, "nom du joueur")
        self.pendu_play_button = bouton(parent, 2, 1, "jouer", self.pendu_game)



    def manage_player(self):
        players_list = get_list_players(save_file)
        player_name = self.select_player_input.get_value()

        if player_name == False:
            player_name = "ANONYME"
            if player_name not in players_list:
                add_player(player_name, save_file)
                self.player = joueur(player_name, 10)
                string = str(f"nom du joueur: {self.player.get_name} // score: {self.player.get_score}")
                self.label_player.config(text=string)

            else:
                n, s = get_score_player_name(player_name, save_file)
                self.player.set_name(n)
                self.player.set_score(s)
                string = str(f"nom du joueur: {self.player.get_name} // score: {self.player.get_score}")
                self.label_player.config(text=string)


        elif player_name in players_list:
            n, s = get_score_player_name(player_name, save_file)
            self.player = joueur(n, s)
            string = str(f"nom du joueur: {self.player.get_name} // score: {self.player.get_score}")
            self.label_player.config(text=string)

        elif player_name not in players_list:
            add_player(player_name, save_file)
            n, s = get_score_player_name(player_name, save_file)
            self.player = joueur(n, s)
            string = str(f"nom du joueur: {self.player.get_name} // score: {self.player.get_score}")
            self.label_player.config(text=string)



    def pendu_game(self):
        mot = mot(tentative=10)


        if self.select_player_input.get_value() == False:
            string = "Renseignez un nom de joueur"
            self.label_player.config(text=string)

        else:
            player_input = self.select_player_input.get_value()
            players = get_list_players(save_file)

            if player_input not in players:
                add_player(player_input, save_file)
                self.player.set_name(player_input)
                self.player.set_score(10)

            else:
                n, s = get_score_player_name(player_input, save_file)
                self.player.set_name(n)
                self.player.set_score(s)

            mot_random = random.choice(words_list)
            mot.set_name(mot_random)

            self.lettre_input = saisie(self.parent, 3, 2, "lettre")
            self.lettre_button = bouton(self.parent, 3, 1, "valider lettre", self.check_lettre)


    def check_lettre(self):
        name = self.mot.get_name()
        tentative = self.mot.get_tentative()

        if tentative != 0:
            a = self.lettre_input.get_value()
            name, tentative  = half_guessed_word(name, a, tentative)
            mot.set_name(name)
            mot.set_tentative(tentative)

            string = f"mot:{name}  \ntentative:{tentative}"
            affichage(self.main_display, string)











    def affichage(self, objet, liste):
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



class lettre():
    def __init__(self, lettre=None):
        self.lettre = lettre

    def get_name(self):
        return self.lettre


    def set_name(self, value):
        self.lettre = value




class mot():
    def __init__(self, name=None, tentative=None):
        self.name = name
        self.tentative = tentative

    def get_name(self):
        return self.name

    def get_tentative(self):
        return self.tentative

    def set_name(self, value):
        self.name = value

    def set_tentative(self, value):
        self.tentative = value

    def lower_tentative(self, value):
        self.tentative = self.get_tentative() - value


class joueur():
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_name(self, value):
        self.name = value

    def set_score(self, value):
        self.score = value



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
        self.saisie_label.grid(row=self.xRow, column=self.yCol, sticky="nsew")


    def get_value(self):
        '''
            Méthode qui récupere la valeur rentrée
        '''
        a = self.saisie.get()
        
        if not a:
            return False
        else:
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
save_file = get_config_element("FILES", "save_file")

root = tk.Tk()
root.title("Jeu du pendu")
root.config(menu=menu_bar(root))
root.geometry("600x200")

interface_main(root)

root.mainloop()