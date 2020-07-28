# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk
from math import ceil
from datetime import timedelta

# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

def test_int(value):
    test = -1
    try:
        int(value)
    except ValueError:
        print("please input integer number (no float).")
        return test
    return int(value)


def test_float(value):
    test = -1
    try:
        float(value)
    except ValueError:
        print("please input float number.")
        return test
    return float(value)



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # init // variables
        self.string01= ""
        self.string02= ""
        self.time_one_PP = ""
        self.time_goal = ""
        self.saisie_point = ""
        self.saisie_goal = ""
        self.saisie_respawn_rate = ""

        # init // boutons
        # self.bouton_clear = bouton(parent, 1, 2, "Clear", self.clear)
        self.bouton_calculer = bouton(parent, 0, 2, "Calculer", self.calculer)

        self.init_input(parent)

    def init_input(self, parent):
        self.saisie_point = saisie(parent, 0, 0,"point")
        self.saisie_goal = saisie(parent, 1, 0, "goal")
        self.saisie_respawn_rate = saisie(parent, 2, 0, "respawn rate")
        self.affichage_output = texte(parent, 4, 0, 50, 3)


    def calculer(self):
        p = self.saisie_point.get()
        g = self.saisie_goal.get()
        r = self.saisie_respawn_rate.get()

        time_01_pp, time_goal = self.calcul(p, g, r)

        self.string01 = f"Temps passé pour avoir 1 PP: {time_01_pp} hh:mm:ss"
        self.string02 = f"Temps passé pour avoir {g} PP: {time_goal} hh:mm:ss"
        self.display( self.string01 + '\n' + self.string02)




    def calcul(self, point, goal, respawn_rate):
        respawn_rate += 0.8
        progress = test_int(1000000/point)
        time_one_pp = progress*respawn_rate
        time_one_pp = time_one_pp
        time_goal = goal*time_one_pp
        # génération de valeur temporelles, attribution en variable
        time_one_pp = timedelta(seconds=time_one_pp)
        time_goal = timedelta(seconds=time_goal)
        return time_one_pp, time_goal





    def display(self, text_):
        self.affichage_output.config(state=tk.NORMAL)
        self.affichage_output.delete('1.0', tk.END)
        self.affichage_output.insert('1.0', text_)
        self.affichage_output.config(state=tk.DISABLED)





class saisie(tk.Entry):
    def __init__(self, parent, xRow, yCol, label=None):
        tk.Entry.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.label = label

        self.s = tk.Entry(parent)
        self.s.grid(row=self.xRow, column=self.yCol+1)

        self.s_label = tk.Label(parent, text=self.label)
        self.s_label.grid(row=self.xRow, column=self.yCol, sticky="w")





class texte(tk.Text):
    def __init__(self, parent, xRow, yCol, w, h):
        tk.Text.__init__(self, parent)
        self.xRow = xRow
        self.yCol = yCol
        self.width = w
        self.height = h

        self.boite_texte = tk.Text(parent, width=self.width, height=self.height, state=tk.DISABLED)
        self.boite_texte.grid(row=self.xRow, column=self.yCol, columnspan=3)





class bouton(tk.Button):
    def __init__(self, parent, xRow, yCol, titre, cmd):
        tk.Button.__init__(self)
        self.bouton = tk.Button(parent, text=titre, height=1, width=7, command=cmd)
        self.xRow = xRow
        self.yCol = yCol
        self.bouton.grid(row=self.xRow, column=self.yCol)




class menu_bar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self,parent)

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





class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        visuel = interface(self)
        menuBar = menu_bar(self)
        self.config(menu=menuBar)


        self.title("Perk Points Calculator")
        self.iconbitmap("pp_calculator_poo/logo.ico")





# ==================================================================================================
#   SCRIPT
# ==================================================================================================

app = Application()
app.mainloop()
