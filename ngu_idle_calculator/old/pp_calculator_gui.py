# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

from math import ceil
from datetime import timedelta

import tkinter as tk

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

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




# points gagnés par kill
def nb_point_progres():
    point2PP = input("input progress point to next perk point: ")
    point2PP = test_int(point2PP)
    if point2PP == -1:
        nb_point_progres()
    return point2PP


# temps en secondes passé pour tuer un enemi
def Input_4_One_Kill():
    time2Kill = input("input time to kill enemy (expressed in seconds): ")
    time2Kill = test_float(time2Kill)
    if time2Kill == -1:
        Input_4_One_Kill()
    return time2Kill


# nombre de PP souhaité
def nb_PP_wished():
    nbPPWished = input("input number of PP you aim for: ")
    nbPPWished = test_int(nbPPWished)
    if nbPPWished == -1:
        nb_PP_wished()
    return nbPPWished


# nb d'enemis tués pour avoir un PP
def nb_enemy_1_PP(progressPoint):
    nbKill = ceil(1000000/progressPoint)
    nbKill = test_int(nbKill)
    if nbKill == -1:
        nb_enemy_1_PP(progressPoint)
    return nbKill


# temps passé pour avoir un PP
def time_to_01_pp(nb,time):
    returnTime = nb*time
    returnTime = test_float(returnTime)
    if returnTime == -1:
        time_to_01_pp(nb,time)
    return returnTime


# ===================================================================================================
#   FONCTIONS
# ===================================================================================================

def pp_progress_calculator():
    nb_point = point_progres.get()
    nb_point = test_int(nb_point)
    time_per_enemy = time_01_tgt.get()
    time_per_enemy = test_float(time_per_enemy)
    pp_tgt = pp_aimed.get()
    pp_tgt = test_int(pp_tgt)

    nb_enemy = nb_enemy_1_PP(nb_point)
    time = time_to_01_pp(nb_enemy, time_per_enemy)

    return time, pp_tgt

def output_time():
    time, pp_tgt = pp_progress_calculator()
    time2NextPP = timedelta(seconds=ceil(time))
    time2_N_PP = timedelta(seconds=time*pp_tgt)

    global time_1_pp_title
    global time_N_PP_tittle
    time_1_pp_title = tk.Label(time_output, text=f"Temps passé pour avoir 1 PP: {time2NextPP}  hh:mm:ss", bg='white')
    time_1_pp_title.pack()


    time_N_PP_tittle = tk.Label(time_output, text=f"Temps passé pour avoir {pp_aimed.get()} PP: {time2_N_PP}  hh:mm:ss", bg='white')
    time_N_PP_tittle.pack()


    calculator.config(state=tk.DISABLED)


def clear():
    time_1_pp_title.pack_forget()
    time_N_PP_tittle.pack_forget()
    calculator.config(state=tk.NORMAL)



# ===================================================================================================
#   GUI
# ===================================================================================================

#=====
# main
#=====
w = 500
h = 200

window = tk.Tk()
window.title("PP Caculator")
window.geometry(f"{w}x{h}")


#===============
# left container
#===============

left_container = tk.Frame(window, width=200, height=100)
left_container.grid(row=0, column=0, sticky='n')

point_progres_title = tk.Label(left_container, text="nombre de point gagné par KO")
point_progres_title.pack()
point_progres = tk.Entry(left_container)
point_progres.pack()

time_01_tgt_title = tk.Label(left_container, text="temps passé pour faire un KO")
time_01_tgt_title.pack()
time_01_tgt = tk.Entry(left_container)
time_01_tgt.pack()

pp_aimed_title = tk.Label(left_container, text="nombre de PP ciblé")
pp_aimed_title.pack()
pp_aimed = tk.Entry(left_container)
pp_aimed.pack()


# ---------- button left container  ----------
# boutton pour calculer et afficher le résultat
calculator = tk.Button(left_container, text="Calculer", command=output_time)
calculator.pack()

# boutton pour supprimer l'affichage du résultat
clear_button = tk.Button(left_container, text="Clear", command=clear)
clear_button.pack()


#=================
# center container
#=================
center_container = tk.Frame(window, width=200, height=100)
center_container.grid(row=0, column=1, sticky='n')

time_output = tk.Frame(center_container, bg='white')
time_output.pack()




# MENU
menu_bar = tk.Menu(window)

menu_acceuil = tk.Menu(menu_bar, tearoff=0)
menu_acceuil.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(menu=menu_acceuil, label="Acceuil")

menu_option = tk.Menu(menu_bar, tearoff=0)
menu_option.add_command(label="Resolution")
menu_bar.add_cascade(menu=menu_option, label="Settings")

window.config(menu=menu_bar)

# affichage
window.mainloop()

