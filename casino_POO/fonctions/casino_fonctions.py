# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import time

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def test_int(value):
    """
        Arguments:
        value: valeur à tester en tant que integer

        but: tester si l'argument est un chiffre entier.
        return: la valeur passé en argument en int()
    """
    
    try:
        value = int(value)
    except ValueError:
        print("Saisissez un chiffre.")
    return value


def start_money():
    """
        Saisie du montant d'argent de départ. Contrôle du montant. 
        
        Arguments:
        nom: start_money

        return: le montant d'argent de départ
    """
    

    moneystart = -1
    print("Vous décidez d'aller au casino")
    while moneystart <=0 or moneystart > 100:
        moneystart = input("Saissisez un montant de départ compris entre 1 et 100: ")
        moneystart = test_int(moneystart)
        
        if moneystart == 666:
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")

        elif moneystart == 777:
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            break

    return moneystart




def caseMiser(max, min = 0):
    """
        Saisie du numéro decase sur laquelle miser
        
        Arguments:
        max: 
        min: 
        return: le nombre de la case sur laquelle le joueur mise
    """
    numCase = -1

    while numCase < min or numCase > max:
        numCase = input("Saisissez le chiffre sur lequel vous misez: ")
        numCase = test_int(numCase)
        
        if numCase < min or numCase > max:
            print("Saisissez un nombre compris entre ", min, " et ", max, " .")

    return numCase



def montantMiser(money):
    """
        Le joueur saisi le montant d'argent à miser. Controle du montant
        
        Arguments:
        money: le montant d'argent du joueur

        return:la somme d'argent que le joueur souhaite miser.
    """
    mise = -1

    while mise <= 0 or mise > money:
        mise = input("Saisissez le montant à miser: ")
        mise = test_int(mise)
        
        if mise <= 0 or mise > money:
            print("Merci de saisir un montant supérieur à zéro et inférieur ou égal à ", money, ".")

    return mise



def opt_roulette_max():
    """
        L utilisateur determine ou nom le nombre de case maximum de la roulette
    """

    y_n = -1

    while y_n < 1 or y_n > 2:
        y_n = input("Voulez-vous définir le nombre maximum de case de la roulette?  1) Oui   2) Non: ")
        y_n = test_int(y_n)
        if y_n == 1:
            case = input("Saisissez le nombre maximum de case de votre roulette: ")
            case = test_int(case)
            return case
        elif y_n == 2:
            return 50
        else:
            print("saisissez 1  pour oui ou 2 pour non")
    

