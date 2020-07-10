# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import time
import random
import math

from classes import money_class
from fonctions.casino_fonctions import start_money
from fonctions.casino_fonctions import caseMiser
from fonctions.casino_fonctions import montantMiser

# ==================================================================================================
#   Script
# ==================================================================================================

# création de l'objet représentant l'argent du joueur
money_start = money_class.money(start_money())


print()
time.sleep(1)
print("Vous voilà au casino.")
time.sleep(1)
print("RECTIFICATION: vous voilà dans un casino où il n'y a que des roulettes !")
time.sleep(1)
print("Vous vous asseyez à une table.")

#initialisation du controleur de la boucle de jeu
jouer = True

# debut de la boucle de jeu
while jouer == True:
    print()
    time.sleep(1)
    mise = montantMiser(money_start.amnt)
    caseCible = caseMiser()
    caseBille = random.randrange(50)
    print("Vous misez ", mise," Brouzoufes sur le chiffre ", caseCible)

    if caseBille == caseCible:
        gagne = mise * 3
        money_start.amnt_increase(gagne)
        print("Vous gagnez ", mise*3,". Argent restant: ", money_start.amnt)

    elif caseBille % 2 == caseCible % 2:
        gagne = math.ceil(mise * 0.5)
        money_start.amnt_increase(gagne)
        print("Vous gagnez ", gagne,". Argent restant: ", money_start.amnt)

    else:
        money_start.amnt_decrease(mise)
        print("Vous perdez ", mise,". Argent restant: ", money_start.amnt)

    print("Il vous reste ", money_start.amnt,".")
    keepPlay = input("Saouhaitez vous continuer à jouer? 1) Oui  2) Non: ")
    
    try:
        keepPlay = int(keepPlay)
    except ValueError:
        print("Saisissez un chiffre.")
    
    if keepPlay == 2:
        print("Vous quittez le Casino")
        time.sleep(1)
        jouer = False

    else:
        print()
        print("Et c'est reparti pour un tour !")
        print()

print("Vous rentrez chez vous")
exit()