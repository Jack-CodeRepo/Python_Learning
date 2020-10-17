# -*- coding: utf-8 -*-
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
    Le fichier est spécifié en variable globale

    :return: le contenu du fichier
    :rtype: list
    """

    f = open(fichier, "r")
    lignes = f.readlines()
    f.close()

    return lignes





def _get_index_from_column_name(fichier, column):
    """
    recupere le numéro d'index par rapport au nom de la colonne

    :param fichier: contenu du fichier
    :type fichier: list
    :param column: nom de la colonne ciblée pour la recherche
    :type column: str
    :return: numéro d'index
    :rtype: int
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

    :param v: nom générique de la valeur cherchée pour l'afficher dans le terminal
    :type v: string
    :return: la valeur saisie
    :rtype: string
    """

    value = input(f"Type the {v} to be searched: ")
    return value





def output_column_name(fichier):
    """
    Affiche le nom et le numero de la colonne

    :param fichier: contenu du fichier
    :type fichier: list
    """

    n = 1
    for name in fichier[0].split(";"):
        print(f"Le nom de la colonne {n} est: {name}")
        n += 1





def get_line_containing_value(fichier, column: str, value: str):
    """
    Permet de chercher une valeure (string) spécifiée dans une colonne spécifiée (nom de colonne)

    :param fichier: contenu du fichier
    :type fichier: list
    :param column: nom de la colonne ciblée pour la recherche
    :type column: str
    :param value: valeur recherchée
    :type value: str
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
                    print(f"valeur \"{value}\" trouvee dans {line} à l'index {index}. \nLe numero de colonne est {column_number}.\n")
                    write_line_in_file(line, output_file)
            
            i += 1

            # reset de l'index de controle si la boucle arrive à la derniere colonne
            if i == len(line.split(";")):
                i = 0





def write_line_in_file(line, fichier):
    """
    ecrire une ligne dans un fichier

    :param line: ligne à écrire
    :type line: string
    :param fichier: fichier dans lequel ecrire
    :type fichier: string
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

