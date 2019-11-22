# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   INPORT
# ===================================================================================================

import time


# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

# def Go_Sleep():
#     time.sleep(2)
#     print("Vous allez dormir.")
#     time.sleep(5)
#     print("Bonne Nuitée !")
#     time.sleep(5)
#     print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")



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
            money = 0
        elif money == 777:
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            print("Vous partez de chez vous avec ", money, " Brouzoufes.")
            print("=>")
            break
        else:
            print("Vous partez de chez vous avec ", money, " Brouzoufes.")
            print("=>")




def Go_Bar():
    print("Off I Go.")



def Go_Whores():
    print("Let's go beaches!")



def casino():
    time.sleep(3)
    print("============================================================")
    print("Vous voilà au casino.")
    time.sleep(3)
    print("RECTIFICATION: vous voilà dans un casino où il n'y a que des roulettes !")



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
            Go_Sleep()
        if activity == 2:
            Pick_Money()
            Go_Bar()
        if activity == 3:
            Pick_Money()
            Go_Whores()
        if activity == 4:
            Pick_Money()
            casino()

