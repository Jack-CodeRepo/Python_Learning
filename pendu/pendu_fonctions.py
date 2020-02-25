# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

import os
import re
import random
import string

import pendu_donnees

# ===================================================================================================
#   Declarations des fonctions
# ===================================================================================================

# les deux fonctions joueurExist et checkFile gère le fichier de score et vérifie si le joueur est déjà présent dans le fichier de score
def joueurExist(playerName,fichier):
    f = open(fichier, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if playerName in line:
            score = line.split(".")[1].strip()
            print("Le joueur", playerName, "a été trouvé et a un score de ", score, " points")
            return int(score)
    f = open("score", "a")
    f.write(playerName + ".0\n")
    print("Le joueur ", playerName," a ete ajoute au fichier de sauvegarde")
    f.close()
    return int(0)

def checkFile(playerName):
    if not os.path.exists("score"):
        f = open("score", "w")
        print("Le fichier de sauvegarde a été créé")
        print("Le joueur ", playerName," a ete ajoute au fichier de sauvegarde")
        f.write(playerName + ".0\n")
        f.close()
        return int(0)
    elif os.path.exists("score"):
        score = joueurExist(playerName,"score")
        return int(score)



# affiche la saisie d'une lettre et renvoi la la valeur de la saisie
def chose_letter():
    letterPick = input("Saisissez la lettre: ")
    try:
        letterPick = str(letterPick)
    except ValueError:
        print("merci de saisir une lettre")
    if len(letterPick) !=1:
            print("vous avez renseigné plsuieurs charactere. merci de saisir une seule lettre.")
    return letterPick


# controle si la lettre est présent dans la string éword" spécifiée en argument

def le_jeu_du_pendu:
    
    print("Vous jouez au pendu")
    name = input("Renseignez votre nom: ")

    score = pendu_fonctions.checkFile(name)

    print("nom du joueur est: ", name, "et son score est: ", score)

    word = random.choice(pendu_donnees.listeMots)
    lgtWord = len(word)
    print("Le mot à deviner contient ", lgtWord, "lettres.")

    hiddenword = ""
    for i in range(0, lgtWord):
        hiddenword += "_"

    letterPickList = []
    letterPick = pendu_fonctions.chose_letter()
    letterPickList += letterPick

    hiddenword, score = letter_check(hiddenword, score)


def letter_check(hiddenword, score):
    result = ""
    if letterPick in word:
        score += 1
        for i in range(0, lgtWord):
            if word[i] == letterPick:
                result += letterPick
            else:
                result += hiddenword[i]
        return result, score
    else:
        if score == 0:
            return word, score
        else:
            score -= 1
            return word, score






# ===================================================================================================
#   Script
# ===================================================================================================

