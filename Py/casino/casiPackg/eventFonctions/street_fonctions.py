# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time
from .home_fonctions import Go_Sleep
from .casino_fonctions import casino
from .dames_fonctions import Go_Whores
from .bar_fonctions import Go_Bar

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def Go_Street(money):
    Out = -1

    while Out == -1:
        money = money
        print("Vous sortez et vous retrouvez dans la rue.")
        time.sleep(1)
        print("Saisissez ce que vous souhaitez faire:")
        activity = input("1) Rentrez chez vous  2) Aller au Bar  3) Aller voir les Dames_Qui_Vendent_Du_Bonheur  4) Aller au Casino: ")
        print("    ")
        try:
            activity = int(activity)
        except ValueError:
            print("Saisissez un chiffre.")
            activity = -1
        if activity == 1:
            Go_Sleep()
        if activity == 2:
            Go_Bar(money)
        if activity == 3:
            Go_Whores(money)
        if activity == 4:
            casino(money)



# ===================================================================================================
#   Script
# ===================================================================================================

