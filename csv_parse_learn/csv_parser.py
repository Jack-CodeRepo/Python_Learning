#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import csv
import sys
import os

# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

# source_file = "csv_test.csv"

source_file = sys.argv[1]

output_file = "output.csv"


# ==================================================================================================
#   DICT
# ==================================================================================================

column_index = {"numero":0, "type_voie":1, "nom_voie":2,
    "code_postal":3, "nom_ville":4, "num_dept":5 ,
    "nom_dept":6, "region":7, "pays":8
    }


# ==================================================================================================
#   LISTS
# ==================================================================================================



# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

def get_file(fichier):
    """
    Ouvre le fichier csv_test.csv en mode lecture

    Parameters
    ----------
    fichier :
        Le fichier à ouvrir.

    Returns
    -------
    str
        le contenu du fichier
    """

    f = open(fichier, "r")
    lignes = f.readlines()
    f.close()

    return lignes





def _get_index_from_column_name(fichier, column: str):
    """
    recupere le numéro d'index par rapport au nom de la colonne

    Parameters
    ----------
    fichier : list
        contenu du fichier
    column : str
        nom de la colonne ciblée pour la recherche

    Returns
    -------
    int
        numéro d'index
    """

    line_01 = fichier[0].split(";")
    index = 0
    for c in line_01:
        if column in c:
            return index
        index += 1





def input_to_search(v):
    """
    lance une invite de saisie

    Parameters
    ----------
    v : str
        nom générique de la valeur cherchée pour l'afficher dans le terminal

    Returns
    -------
    str
        la valeur saisie
    """

    value = input(f"Type the {v} to be searched: ")
    return value





def output_column_name(fichier):
    """
    Affiche le nom et le numero de la colonne

    Parameters
    ----------
    fichier : list
        contenu du fichier
    """

    n = 1
    for name in fichier[0].split(";"):
        print(f"Le nom de la colonne {n} est: {name}")
        n += 1





def get_line_containing_value(fichier, column: str, value: str):
    """
    Permet de chercher une valeure (str) spécifiée dans une colonne spécifiée (nom de colonne)
    
    Parameters
    ----------
    fichier : list
        contenu du fichier
    column : str
        nom de la colonne ciblée pour la recherche
    value : str
        valeur recherchée
    """

    index = _get_index_from_column_name(fichier, column)
    column_number = index + 1

    i = 0
    for line in fichier:
        line_list = line.split(";")
        for col in line_list:
            # verifie que l'index de controle correspond à l'index de la colonne ciblée
            if i == index:
                if value in col:
                    print(f"valeur \"{value}\" trouvee dans:\n {line}L'index est: {index}.\nLe numero de colonne est {column_number}.\n")
                    write_line_in_file(line, output_file)
            
            i += 1

            # reset de l'index de controle si la boucle arrive à la derniere colonne
            if i == len(line.split(";")):
                i = 0





def write_line_in_file(line, fichier):
    """
    ecrire une ligne dans un fichier

    Parameters
    ----------
    line : str
        ligne à écrire
    fichier : str
        fichier dans lequel ecrire
    """

    if os.path.isfile(fichier):
        with open(fichier, "a+") as f:
            f.write(line)
    else:
        with open(fichier, "w+") as f:
            f.write(line)





# ==================================================================================================
#   CLASSES
# ==================================================================================================


# ==================================================================================================
#   SCRIPT
# ==================================================================================================


if __name__ == "__main__":

    fileSource = get_file(source_file)
    output_column_name(fileSource)
    input()
    
    value = input_to_search("value")
    column = input_to_search("column")
    input()
    
    get_line_containing_value(fileSource, column , value)

