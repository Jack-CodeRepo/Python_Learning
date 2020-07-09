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
    while moneystart <=0 or moneystart > 100:
        print()
        moneystart = input("Saissisez un montant de départ compris entre 1 et 100: ")
        try:
            moneystart = int(moneystart)
        except ValueError:
            time.sleep(1)
            print()
            print("Saisissez un chiffre.")
            moneystart = -1
        if moneystart == 666:
            time.sleep(1)
            print()
            print("C'est le nombre d'un homme. Relisez l'Apocalypse de Saint Jean.")
            moneystart = -1
        elif moneystart == 777:
            time.sleep(1)
            print()
            print("Ca porte bonheur. Vous pouvez prendre ce montant. Bonne chance.")
            break
    return moneystart
