# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import os
import re

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

def checkFile():
    nomFichier = "score"
    if os.path.isfile(nomFichier):
        return nomFichier
    else:
        fichier = open("score", "a")
        print("Le fichier ", fichier, " a été créé")
        fichier.close()
        return fichier

def joueurExist(playerName,fichier):
    f = open("fichier", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if playerName in line:
            score = line.split(".")[1].strip()
            print("Le joueur", playerName, "a été trouvé et a un score de ", score, " points")
            fichier.close()
            return score
        else:
            f.write(playerName+".8")
            return 8



# ===================================================================================================
#   Script
# ===================================================================================================

