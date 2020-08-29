# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from datetime import timedelta
from math import ceil

# ==================================================================================================
#   FONCTIONS
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.time_un_pp = ""
        self.time_goal = ""
        self.output = ""

        self.calculer_temps_bouton = bouton(parent, 0, 2 , "Calculer le temps", self.calculer_temps)
        self.clear_bouton = bouton(parent, 2, 2, "Clear", self.clear)
        self.calculer_PP_bouton = bouton(parent, 1, 2, "Calculer les PP", self.calculer_PP)

        self.saisie_point = saisie(parent, 0, 0, "point")
        self.saisie_respawn = saisie(parent, 1, 0,"Respawn rate (seconds)")
        self.saisie_goal = saisie(parent, 2, 0, "goal")
        self.saisie_goal_time = saisie(parent, 3, 0, "time aimed (hour)")
        self.output = texte(parent, 4, 0, 50, 3).get_text()



    def calculer_PP(self):
        # calcul du temps pour 1 PP
        time_01_pp = self.time_one_pp()
        t_aimed = self.saisie_goal_time.test_int(self.saisie_goal_time.get_value())
        pp_per_min = 60/time_01_pp
        pp_per_hour = 60*pp_per_min
        result = ceil(pp_per_hour*t_aimed)
        self.pp_earned = result



        # a chaque calcul, deux lignes de message sont générées et affichées
        string01 = f"{self.pp_earned} PP gagné en {t_aimed} heures."
        self.display( string01)



    def calculer_temps(self):
        g = self.saisie_goal.test_int(self.saisie_goal.get_value())
        t = self.time_one_pp()
        time_01_pp = ceil(t)
        time_goal = ceil(g * t)
        # génération de valeur temporelles, attribution en variable
        self.time_un_pp = timedelta(seconds=time_01_pp)
        self.time_goal = timedelta(seconds=time_goal)

        # a chaque calcul, deux lignes de message sont générées et affichées
        string01 = f"Temps passé pour avoir 1 PP: {self.time_un_pp} hh:mm:ss"
        string02 = f"Temps passé pour avoir {g} PP: {self.time_goal} hh:mm:ss"
        self.display( string01 + '\n' + string02 )



    def time_one_pp(self):
        p = self.saisie_point.test_int(self.saisie_point.get_value())
        r = self.saisie_respawn.test_float(self.saisie_respawn.get_value())
        t = r + 0.8

        progress = 1000000/p
        time_one_pp = progress*t

        return time_one_pp



    def display(self, text):
        self.output.config(state=tk.NORMAL, font="Calibri")
        self.output.delete('1.0', tk.END)
        self.output.insert('1.0', text)
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
        self.saisie.grid(row=self.xRow, column=self.yCol+1)
        # création du nom de la zone de saisie (label)
        self.saisie_label = tk.Label(parent, text=self.label)
        self.saisie_label.grid(row=self.xRow, column=self.yCol, sticky="w")



    def get_value(self):
        '''
            Méthode qui récupere la valeur rentrée
        '''
        return self.saisie.get()



    def test_int(self,value):
        try:
            int(value)
        except ValueError:
            self.saisie.delete(0, tk.END)
        return int(value)



    def test_float(self, value):
        try:
            float(value)
        except ValueError:
            self.saisie.delete(0, tk.END)
        return float(value)





class texte(tk.Text):
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
        menu_Fichier.add_command(label="Ouvrir")
        menu_Fichier.add_command(label="Enregistrer")
        menu_Fichier.add_command(label="Enregistrer Sous")
        menu_Fichier.add_command(label="Imprimer")
        menu_Fichier.add_separator()
        menu_Fichier.add_command(label="Quitter", command=self.quitter)

        menu_Help = tk.Menu(self, tearoff=0)
        menu_Help.add_command(label="Documentation")
        menu_Help.add_command(label="Mail au support")

        self.add_cascade(label="Fichier", menu=menu_Fichier)
        self.add_cascade(label="Help", menu=menu_Help)



    def quitter(self):
        exit()





# ==================================================================================================
#   SCRIPT
# ==================================================================================================

# définition de la fenetre principale 'root'
root = tk.Tk()

# configuration de la fenetre principale
# association du menu de la fenetre principale 'root' par appel de la class 'menu_bar'
root.config(menu=menu_bar(root))
# définition du titre de la fenetre principale 'root'
root.title("Perk Points Calculator")
# définition du logo de la fenetre principale 'root'
root.iconbitmap("pp_calculator_poo/logo.ico")
# association des éléments GUI à root par appel de la class 'interface'
interface(root)

# génération du GUI
root.mainloop()
