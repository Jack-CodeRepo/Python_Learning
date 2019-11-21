# -*- coding: utf-8 -*-

import os
import random
import math
import time

mise = -1

def Pick_Money():
    money = -1
    print("Vous décidez de sortir et de prendre de l'argent.")
    while money <= 0 or money > 100 or money == 777:
        print("============================================================")
        money = input("Saissisez un montant de départ compris entre 1 et 100:: ")
        print("=>")
        try:
            money = int(money)
        except ValueError:
            print("Saisissez un chiffre.")
            money = -1
        if money == 666:
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            money = -1

        if money == 777:
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            print("Vous partez de chez vous avec ", money, " Brouzoufes.")
            casino()

    print("Vous partez de chez vous avec ", money, " Brouzoufes.")
    casino()

def Go_Sleep():
    print("Vous allez dormir.")
    print("Bonne Nuitée !")


def Go_Out():
    print("Vous vous ennuyez.")
    time.sleep(5)
    print("Vous vous ennuyez. BEAUCOUP")
    time.sleep(5)
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
            Go_Bar()
        if activity == 3:
            Go_Whores()
        if activity == 4:
            casino()

def Go_Bar():
    Pick_Money()

def Go_Whores():
    Pick_Money()

def casino():
    Pick_Money()
    print("Vous voilà au casino.")
    time.sleep(2)
    print("RECTIFICATION: vous voilà dans un casino où il n'y a que des roulettes !")





Go_Out()
