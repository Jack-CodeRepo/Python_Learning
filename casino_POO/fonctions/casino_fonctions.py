# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================


def start_money():
    """
        nom: start_money
        but: demande à l'utlisateur de saisir le montant de départ voulu et gère les exceptions
    """
    

    moneystart = -1
    print()
    print("Vous décidez d'aller au casino")
    while moneystart <=0 or moneystart > 100:
        time.sleep(1)
        print()
        moneystart = input("Saissisez un montant de départ compris entre 1 et 100: ")
        try:
            moneystart = int(moneystart)
        except ValueError:
            time.sleep(1)
            print("Saisissez un chiffre.")
            moneystart = -1
        if moneystart == 666:
            time.sleep(1)
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            moneystart = -1
        elif moneystart == 777:
            print()
            time.sleep(1)
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            break
    return moneystart




def caseMiser():
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


