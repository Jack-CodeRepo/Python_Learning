
# from model.cls01 import teacher

from model import cls01
from time import sleep


if __name__ in __name__ == "__main__":
    
    print("premier professeur créé")
    prof01 = cls01.teacher("StreetCred", "Bobby", "10", "ambigu")
    print("prof01   nom: ", prof01.name,"/ prenom: ", prof01.lastName, "/ craie: ", prof01.craie, "/ sexe: ", prof01.sexe)
    input("appuyer sur un touche pour continuer")
    print()

    print("second professeur créé")
    prof02 = cls01.teacher("Pondbeef","Jack", "0", "No One Knows")
    print("prof02   nom: ", prof02.name, "/ prenom: ", prof02.lastName, "/ craie: ", prof02.craie, "/ sexe: ", prof02.sexe)
    input("appuyer sur un touche pour continuer")
    print()

    print("Troisieme professeur créé")
    prof03 = cls01.teacher("Prof", "Instit", "2", "Neutre")
    print("prof03   nom: ", prof03.name, "/ prenom: ", prof03.lastName, "/ craie: ", prof03.craie, "/ sexe: ", prof03.sexe)
    input("appuyer sur un touche pour continuer")
    print()

    print("Nous avons créé trois objets \"prof01\"  \"prof02\"  \"prof03\"")
    input("appuyer sur un touche pour continuer")
    print()

    print("on modifie la valeur de l'attribu \"craie\" de l'objet prof01")
    print("prof01.craie = prof01.craie + 10")
    prof01.craie = prof01.craie + 10
    print("le nombre de craie de ", prof01.name, " est ", prof01.craie)
    input("appuyer sur un touche pour continuer")
    print()

    print("On attribue à l'objet \"prof01\" les attributs de \"prof02\" avec le code : ")
    print("prof01 = prof02")
    prof01 = prof02
    input("appuyer sur un touche pour continuer")
    print()

    print("On affiche à nouveau les attributs de l'objet prof01")
    print("nom: ", prof01.name,"/ prenom: ", prof01.lastName, "/ craie: ", prof01.craie, "/ sexe: ", prof01.sexe)
    print("Les attributs de l'objet \"prof01\" ont été changée avec les valeurs des atributs de l'objet \"prof02\"")
    input("appuyer sur un touche pour continuer")
    print()

    print("On modifie à nouveau les attributs de l'objet \"prof01\" en prenant les attributs de \"prof03\" avec le code : ")
    print("prof01 = prof03")
    prof01 = prof03
    input("appuyer sur un touche pour continuer")
    print()

    print("On affiche à nouveau les attributs de l'objet prof01")
    print("nom: ", prof01.name,"/ prenom: ", prof01.lastName, "/ craie: ", prof01.craie, "/ sexe: ", prof01.sexe)
    print("Les attributs de l'objet \"prof01\" ont été changée avec les valeurs des atributs de l'objet \"prof03\"")
    input("appuyer sur un touche pour continuer")
    print()


if not __name__ in __name__ == "__main__":
    print("Aujourd'hui il fait grand soleil.")


# if not __name__ in __name__ == "__main__":
#     print("MDR LA VIE C'EST COMME LE SOLEIL CA VA DISPARAITRE")
