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
        print("please input integer number (no float).")
        return test
    return float(value)

# ==================================================================================================
#   CLASSES
# ==================================================================================================

class pp_calculator:

    # ---------- construtor DEBUT ----------
    def __init__(self, parent, x, y):
        self.parent = parent
        
        # init // variables utilisées par le calcul
        self.goal = ""
        self.time = ""
        self.point = ""
        self.time_one_pp = ""
        self.time_goal = ""

        # init // variables contenant les messages d'output
        self.string01= ''
        self.string02=''

        # init // widget contenant grids
        self.contenant = tk.Frame(self.parent)
        self.contenant.grid(row=x, column=y)

        self.button_width = 7
        self.button_height = 1

        # init // variables contenant les input
        self.io01 = ""
        self.io02 = ""
        self.io03 = ""

        # widget de saisie
        self.entry(0,0)

        # widget affichage de l'ouput
        self.entry_output_cell(3,0)

        # init // boutons
        self.button_calculer_click("calculer", 0, 2)
        self.button_clear_click("Clear", 1, 2)

    # ---------- construtor FIN ----------



    # fonction qui gere et affiche les widget de saisie
    def entry(self, x, y):
        # 1er widget de saisie
        self.i01 = tk.Entry(self.contenant, width=10)
        self.i01.grid(row=x, column=y+1)
        self.i01_label = tk.Label(self.contenant, text="point")
        self.i01_label.grid(row=x, column=y)
        # 2nd widget de saisie
        self.i02 = tk.Entry(self.contenant, width=10)
        self.i02.grid(row=x+1, column=y+1)
        self.i02_label = tk.Label(self.contenant, text="goal")
        self.i02_label.grid(row=x+1, column=y)
        # 3eme widget de saisie
        self.i03 = tk.Entry(self.contenant, width=10)
        self.i03.grid(row=x+2, column=y+1)
        self.i03_label = tk.Label(self.contenant, text="time")
        self.i03_label.grid(row=x+2, column=y)


    # fonction qui gere la fenetre d'output
    def entry_output_cell(self, x, y):
        self.o = tk.Text(
            self.contenant, font=10, state=tk.DISABLED,
            height=3, width=50)
        self.o.grid(row=x, column=y, columnspan=3)


    # fonction réalisant les calculs et affiche les messages
    def calculer(self):
        # on récupere les inputs et les attribue dans des variables
        # chaque variables est testée puis typée
        self.point = self.i01.get()
        self.point = test_int(self.point)
        self.goal = self.i02.get()
        self.goal = test_int(self.goal)
        self.time = self.i03.get()
        self.time =test_float(self.time)
        # calcul
        progress = test_int(1000000/self.point)
        time_one_pp = progress*self.time
        time_one_pp = ceil(test_int(time_one_pp))
        time_goal = self.goal*time_one_pp
        # génération de valeur temporelles, attribution en variable
        self.time_one_pp = timedelta(seconds=time_one_pp)
        self.time_goal = timedelta(seconds=time_goal)
        # a chaque calcul, deux lignes de message sont générées et affichées
        self.string01 = f"Temps passé pour avoir 1 PP: {self.time_one_pp} hh:mm:ss"
        self.string02 = f"Temps passé pour avoir {self.goal} PP: {self.time_goal} hh:mm:ss"
        self.display( self.string01 + '\n' + self.string02)


    # bouton pour activer la fonction calculer
    def button_calculer_click(self, titre, x, y):
        self.b = tk.Button(
            self.contenant, text=titre, command=self.calculer,
            width=self.button_width, height=self.button_height)
        self.b.grid(row=x, column=y)


    # fonction qui enleve les outputs de l'affichage
    def clear(self):
        self.goal = ""
        self.time = ""
        self.point = ""
        self.display('')


    # bouton pour activer la fonction clear
    def button_clear_click(self, titre, x, y):
        self.b = tk.Button(
            self.contenant, text=titre, command=self.clear,
            width=self.button_width, height=self.button_height)
        self.b.grid(row=x, column=y)


    # fonction qui gere l'affichage dans la fentre d'output
    def display(self, text_):
        self.o.config(state=tk.NORMAL)
        self.o.delete('1.0', tk.END)
        self.o.insert('1.0', text_)
        self.o.config(state=tk.DISABLED)







class Appli:
    def __init__(self, master):
        self.master = master

        calc = pp_calculator(self.master, 0, 0)

# ==================================================================================================
#   SCRIPT
# ==================================================================================================

root = tk.Tk()
root.title("Perk Points Calculator")
root.iconbitmap("pp_calculator_poo/logo.ico")
application = Appli(root)

root.mainloop()
