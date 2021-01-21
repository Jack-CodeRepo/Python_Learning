#!/usr/bin/env python
# coding: utf-8
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

chemin_exploreur_defaut = None
chemin_complet_fichier = None


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
    config.read("log_explorer.conf")
    folder = config.get("EXPLORER", "default_path")
    fichier = config.get("EXPLORER", "last_log_open")

    return folder, fichier


def open_file(defaut_folder=None, default_file=None):
    if not defaut_folder:
        defaut_folder = chemin_exploreur_defaut

    if not default_file:
        default_file = chemin_complet_fichier
        if not chemin_complet_fichier:
            path_to_file = tk.filedialog.askopenfilename(initialdir=defaut_folder,
                                                filetypes=[("fichier log", "*.log"),
                                                            ("tout les fichiers", "*.*")
                                                ]
                                                )
        modify_conf("EXPLORER", "last_log_open", path_to_file)

    return path_to_file

def modify_conf(section, option, value):
    config = configparser.ConfigParser()
    config.read("configuration.conf")
    config.set(section, option, value)

    with open("configuration.conf", 'w') as configfile:
        config.write(configfile)



def default_explorer_path():
    chemin_exploreur_defaut = tk.filedialog.askdirectory()
    modify_conf("EXPLORER", "default_path",chemin_exploreur_defaut)



def quitter():
    exit()

# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.string_searched = saisie(parent, 0, 0, "recherche:")
        self.output = output_display(parent, 3, 0, 125, 20).get_text()
        self.rechercher_bouton = bouton(parent, 0, 2, "rechercher", self.search_log)


    def search_log(self):
        fichier = chemin_complet_fichier

        if not chemin_complet_fichier:
            fichier = open_file()

        with open(fichier) as fichier:
            lignes_log = fichier.readlines()
            lignes_trouvees = []
            string_cherchee = self.string_searched.get_value()
            for l in lignes_log:
                if string_cherchee in l:
                    lignes_trouvees.append(l)

            if not lignes_trouvees:
                self.display("Pas de correspondance")
            elif lignes_trouvees:
                self.display(lignes_trouvees)


    def display(self, liste):
        self.output.config(state=tk.NORMAL, font="Calibri")
        self.output.delete('1.0', tk.END)
        for l in liste:
            self.output.insert('1.0', l)
        self.output.config(state=tk.DISABLED)


    def clear(self):
        self.display('')








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




class output_display(tk.Text):
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
        self.boite_texte.grid(row=self.xRow, column=self.yCol, columnspan=10)


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
        menu_Fichier.add_command(label="Ouvrir", command=open_file)
        menu_Fichier.add_command(label="Modifier chemin par defaut", command=default_explorer_path)
        menu_Fichier.add_command(label="Enregistrer")
        menu_Fichier.add_command(label="Enregistrer Sous")
        menu_Fichier.add_command(label="Imprimer")
        menu_Fichier.add_separator()
        menu_Fichier.add_command(label="Quitter", command=quitter)

        menu_Help = tk.Menu(self, tearoff=0)
        menu_Help.add_command(label="Documentation")
        menu_Help.add_command(label="Mail au support")

        self.add_cascade(label="Fichier", menu=menu_Fichier)
        self.add_cascade(label="Help", menu=menu_Help)







# ==================================================================================================
#   SCRIPT
# ==================================================================================================

chemin_exploreur_defaut, chemin_complet_fichier = init_config()


root = tk.Tk()
root.title("log_explorer")
root.config(menu=menu_bar(root))

interface_main(root)

root.mainloop()

