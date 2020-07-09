# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time

from random import randrange
from math import ceil


# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================


def Pick_Money():
    print("Vous decidez de sortir et de prendre de l'argent.")
    money = -1
    while money <=0 or money > 100:
        print()
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


def chiffreMiser():
    chiffreMise = -1
    while chiffreMise == -1:
        chiffreMise = input("Saisissez le chiffre sur lequel vous misez: ")
        try:
            chiffreMise = int(chiffreMise)
        except ValueError:
            print("Saisissez un chiffre.")
            chiffreMise = -1
        if chiffreMise < 0 or chiffreMise > 49:
            print("Saisissez un nombre compris entre 1 et 49.")
            chiffreMise = -1
    return chiffreMise



def montantMiser(money):
    mise = -1
    while mise == -1:
        mise = input("Saisissez le montant à miser: ")
        try:
            mise = int(mise)
        except ValueError:
            print("Saisissez un chiffre.")
            mise = -1
        if mise > money:
            print("Merci de saisir un montant inférieur ou égal à votre nombre Brouzoufes.")
            mise = -1
        if mise <= 0:
            print("Merci de saisir un montant supérieur à zéro.")
            mise = -1
    return mise



def casino(money):
    time.sleep(3)
    print("Vous voilà au casino.")
    time.sleep(3)
    print("RECTIFICATION: vous voilà dans un casino où il n'y a que des roulettes !")
    time.sleep(3)
    print("Vous vous asseyez à une table.")

    jouer = True
    while jouer == True:
        chiffreMise = chiffreMiser()
        mise = montantMiser(money)
        caseBille = randrange(50)
        print("Vous misez ", mise," Brouzoufes sur le chiffre ", chiffreMise)

        if caseBille == chiffreMise:
            money = mise + mise * 3
            print("Vous gagnez votre mise ainsi que ", mise*3," Brouzoufes.")
        elif caseBille % 2 == chiffreMise % 2:
            money = mise + ceil(mise * 0.5)
            print("Vous gagnez votre mise ainsi que ", ceil(mise*0.5)," Brouzoufes.")
        else:
            print("Vous perdez votre mise (", mise," Brouzoufes).")
            money = money - mise
        print("Il vous reste ", money," Brouzoufes.")
        keepPlay = input("Saouhaitez vous continuer à jouer? 1) Oui  2) Non: ")
        try:
            keepPlay = int(keepPlay)
        except ValueError:
            print("Saisissez un chiffre.")
        if keepPlay == 2:
            print("Vous quittez le Casino")
            exit()
            jouer == False
        else:
            print()
            print("Et c'est reparti pour un tour !")
            print()



# ===================================================================================================
#   Script
# ===================================================================================================

money = Pick_Money()

casino(money)