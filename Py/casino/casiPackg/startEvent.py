# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   INPORT
# ===================================================================================================

import time
from eventFonctions import *


# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def Go_Bar():
    print("Off I Go.")



def Go_Whores():
    print("Let's go beaches!")



def Go_Out():
    print("Vous vous ennuyez.")
    time.sleep(3)
    print("Vous vous ennuyez. BEAUCOUP")
    time.sleep(3)
    activity = -1
    while activity == -1:
        print("============================================================")
        print("Saisissez ce que vous souhaitez faire:")
        activity = input("1) Dormir  2) Aller au Bar  3) Aller voir les Dames_Qui_Vendent_Du_Bonheur  4) Aller au Casino: ")
        print("=>")
        try:
            activity = int(activity)
        except ValueError:
            print("Saisissez un chiffre.")
            activity = -1
        if activity == 1:
            eventFonctions.home_fonctions.Go_Sleep()
        if activity == 2:
            eventFonctions.home_fonctions.Pick_Money()
            Go_Bar()
        if activity == 3:
            eventFonctions.home_fonctions.Pick_Money()
            Go_Whores()
        if activity == 4:
            eventFonctions.home_fonctions.Pick_Money()
            eventFonctions.casino_fonctions.casino()

