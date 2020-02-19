# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time
from .pendu_fonctions import pendu

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def film():
    print("FILM_CODEaREVOIR_FILM")



def Go_Sleep():
    time.sleep(2)
    print("Vous allez dormir.")
    time.sleep(5)
    print("Bonne Nuitée !")
    time.sleep(5)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")



def homeActivity():
    home = -1
    while home == -1:
        print("Vous décidez de rester chez vous.")
        print("Que souhaitez vous faire :")
        homeDo = input("1) Regarder un film  2) Jouer au pendu  3) Dormir.")
        try:
            homeDo = int(homeDo)
        except ValueError:
            print("Saisissez un chiffre.")
            homeDo = -1
        if homeDo < 0 or homeDo > 4:
            print("Saisissez un nombre de 1 à 4.")
            homeDo = -1
        if homeDo == 1:
            film()
        if homeDo == 2:
            pendu()
        if homeDo == 3:
            Go_Sleep()


# ===================================================================================================
#   Script
# ===================================================================================================
