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
        f = open("score.txt", "w")
        print("Le fichier de sauvegarde a été créé")
        print("Le joueur ", playerName," a ete ajoute au fichier de sauvegarde")
        f.write(playerName + ".0\n")
        f.close()
    elif os.path.exists("score.txt"):
        joueurExist(playerName,"score.txt")




def joueurExist(playerName,fichier):
    f = open(fichier, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if playerName in line:
            score = line.split(".")[1].strip()
            print("Le joueur", playerName, "a été trouvé et a un score de ", score, " points")
            return score
    f = open("score.txt", "a")
    f.write(playerName + ".0\n")
    print("Le joueur ", playerName," a ete ajoute au fichier de sauvegarde")
    f.close()




# ===================================================================================================
#   Script
# ===================================================================================================

