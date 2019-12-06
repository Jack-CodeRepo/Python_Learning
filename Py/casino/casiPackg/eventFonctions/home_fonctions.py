# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time


# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def Go_Sleep():
    time.sleep(2)
    print("Vous allez dormir.")
    time.sleep(5)
    print("Bonne Nuitée !")
    time.sleep(5)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")



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
            continue
        if money == 666:
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            money = -1
        elif money == 777:
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            print("Vous partez de chez vous avec ", money, " Brouzoufes.")
            print("=>")
            break
    print("Vous partez de chez vous avec ", money, " Brouzoufes.")
    print("=>")