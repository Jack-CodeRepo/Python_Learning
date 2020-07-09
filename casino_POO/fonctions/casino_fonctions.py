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
    
    start_money = -1
    while start_money <=0 or start_money > 100:
        print()
        start_money = input("Saissisez un montant de départ compris entre 1 et 100: ")
        try:
            start_money = int(start_money)
        except ValueError:
            time.sleep(1)
            print()
            print("Saisissez un chiffre.")
            start_money = -1
        if start_money == 666:
            time.sleep(1)
            print()
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            start_money = -1
        elif start_money == 777:
            time.sleep(1)
            print()
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            break
    return start_money
