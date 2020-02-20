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

def checkFile(playerName):
    if not os.path.exists("score.txt"):
        fichier = open("score.txt", "w")
        print("Le fichier de sauvegarde a été créé")
        fichier.write(playerName + ".")
        return fichier
    elif os.path.exists("score.txt"):
        print("Le fichier de sauvegarde existe")
    else:
        print("VDM le_code_plante VDM")


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

