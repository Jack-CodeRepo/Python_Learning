# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time
from .eventFonctions import street_fonctions

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def Pick_Money():
    print("Vous decidez de sortir et de prendre de l'argent.")
    money = -1
    while money <=0 or money > 100:
        print("============================================================")
        money = input("Saissisez un montant de départ compris entre 1 et 100: ")
        time.sleep(3)
        try:
            money = int(money)
        except ValueError:
            print("Saisissez un chiffre.")
            money = -1
        if money == 666:
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            money = -1
            time.sleep(1)
        elif money == 777:
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            time.sleep(1)
            break
    print("Vous partez de chez vous avec ", money, " Brouzoufes.")
    return money

def Go_Sleep():
    time.sleep(2)
    print("Vous allez dormir.")
    time.sleep(5)
    print("Bonne Nuitée !")
    time.sleep(5)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")





def Go_Out():
    print("Vous vous ennuyez.")
    time.sleep(3)
    print("Vous vous ennuyez. BEAUCOUP")
    time.sleep(3)
    activity = -1
    while activity == -1:
        print("============================================================")
        print("Saisissez ce que vous souhaitez faire: ")
        activity = input(" 1) Dormir  2) Sortir: ")
        try:
            activity = int(activity)
        except ValueError:
            print("Saisissez un chiffre.")
            activity = -1
        if activity == 1:
            Go_Sleep()
        if activity == 2:
            money = Pick_Money()
            street_fonctions.Go_Street(money)

