# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time
from random import randrange
from math import ceil
from .home_fonctions import Go_Street
from .home_fonctions import Pick_Money

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def casino():
    time.sleep(3)
    print("============================================================")
    print("Vous voilà au casino.")
    time.sleep(3)
    print("RECTIFICATION: vous voilà dans un casino où il n'y a que des roulettes !")

    jeu = -1
    jeu = input("Voulez-vous jouer à la roulette ? 1) Oui  2) Non: ")
    try:
        jeu = int(jeu)
    except ValueError:
        print("Saisissez un chiffre.")
        jeu = -1
    if jeu == 1:
        play_casino()
    else:
        Go_Street()

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
            print("Saisissez un nombre compris entre et 49.")
            chiffreMise = -1
    return chiffreMise

def montantMiser(moneyPick):
    mise = -1
    while mise == -1:
        mise = input("Saisissez le montant à miser: ")
        try:
            mise = int(mise)
        except ValueError:
            print("Saisissez un chiffre.")
            mise = -1
        if mise > moneyPick:
            print("Merci de saisir un montant inférieur ou égal à votre nombre Brouzoufes.")
            mise = -1
        if mise <= moneyPick:
            print("Merci de saisir un montant supérieur à zéro.")
            mise = -1
    return mise

def play_casino():
    jouer = True
    money = Pick_Money()
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
            print("Vous gagnez votre mise ainsi que ", mise*0.5," Brouzoufes.")
        else:
            print("Vous perdez votre mise (", mise," Brouzoufes).")
            money = money - mise