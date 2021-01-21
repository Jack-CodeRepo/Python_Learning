# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import sys
from math import ceil
from datetime import timedelta

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

# points gagnés par kill
def nb_point_progres():
    cnt = -1
    while cnt == -1:
        point2PP = input("input progress point to next perk point: ")
        cnt = 0
        try:
            int(point2PP)
        except ValueError:
            print("please input integer number (no float).")
            cnt = -1
    return int(point2PP)


# temps en secondes passé pour tuer un enemi
def Input_4_One_Kill():
    cnt = -1
    while cnt == -1:
        time2Kill = input("input time to kill enemy (expressed in seconds): ")
        cnt = 0
        try:
            float(time2Kill)
        except ValueError:
            print("please input float number.")
            cnt = -1
    return float(time2Kill)


# nombre de PP souhaité
def nb_PP_wished():
    cnt = -1
    while cnt == -1:
        nbPPWished = input("input number of PP you aim for: ")
        cnt = 0
        try:
            int(nbPPWished)
        except ValueError:
            print("please input integer number (no float).")
            cnt = -1
    return int(nbPPWished)


# nb d'enemis tués pour avoir un PP
def nb_enemy_1_PP(progressPoint):
    cnt = -1
    while cnt == -1:
        nbKill = ceil(1000000/progressPoint)
        cnt = 0
        try:
            int(nbKill)
        except ValueError:
            print("please input integer number (no float).")
            cnt = -1
    return int(nbKill)


# temps passé pour avoir un PP
def time_to_01_pp(nb,time):
    cnt = -1
    while cnt == -1:
        time = nb*time
        cnt = 0
        try:
            float(time)
        except ValueError:
            print("please input integer number (no float).")
            cnt = -1
    return float(time)


# ===================================================================================================
#   Script
# ===================================================================================================
# premier argument est le nombre de point obtenus par kill
nb_point = int(sys.argv[1])
# second argument est le temps pour un kill exprimé en seconde
time_per_enemy = float(sys.argv[2])
# troisieme argument est le nombre de PP voulu
targetPP = int(sys.argv[3])

if __name__ in __name__ == "__main__":
    nb_enemy_2_01PP = nb_enemy_1_PP(nb_point)
    time = time_to_01_pp(nb_enemy_2_01PP,time_per_enemy)
    time2NextPP = timedelta(seconds=ceil(time))
    time2_N_PP = timedelta(seconds=time*targetPP)

    print("=======================================================")
    print(time2NextPP, " hh:mm:ss required for 1 PP.")
    print(time2_N_PP, " hh:mm:ss required for ", targetPP, " PP.")