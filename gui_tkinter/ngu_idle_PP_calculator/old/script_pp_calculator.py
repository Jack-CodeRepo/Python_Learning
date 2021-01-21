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
#   Script
# ===================================================================================================

nb_point = nb_point_progres()
time_per_enemy = Input_4_One_Kill()
nb_enemy_2_01PP = nb_enemy_1_PP(nb_point)
time = time_to_01_pp(nb_enemy_2_01PP,time_per_enemy)
targetPP = nb_PP_wished()

time2NextPP = timedelta(seconds=ceil(time))
time2_N_PP = timedelta(seconds=time*targetPP)

print("=======================================================")
print(time2NextPP, " hh:mm:ss required for 1 PP.")
print(time2_N_PP, " hh:mm:ss required for ", targetPP, " PP.")


