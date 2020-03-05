
# from model.cls01 import teacher

from model import cls01

if __name__ in __name__ == "__main__":
    prof01 = cls01.teacher("StreetCred", "Bobby", 10, "ambigu")
    print("premier professeur créé (attention il est armé)")
    print("nom: ", prof01.get_name(),"/ prenom: ", prof01.get_lastName(), "/ craie: ", prof01.get_craie(), "/ sexe: ", prof01.get_sexe())
    print()
    print("second professeur créé (attention il est naze, il n'a même pas de craie)")
    prof02 = cls01.teacher("Pondbeef","Jack", 0, "No One Knows")
    print("nom: ", prof02.get_name(), "/ prenom: ", prof02.get_lastName(), "/ craie: ", prof02.get_craie(), "/ sexe: ", prof02.get_sexe())
    print(prof02.get_lastName()," s'exclame \"VIE DE MERDE\"")
    print()
    print("Troisieme professeur créé")
    prof03 = cls01.teacher("Prof", "Instit", 10, "Neutre")
    print("nom: ", prof03.get_name(), "/ prenom: ", prof03.get_lastName(), "/ craie: ", prof03.get_craie(), "/ sexe: ", prof03.get_sexe())
    print()
    print("Test prof01 = prof02")
    prof01 = prof02
    print("On affiche à nouveau les attributs de l'objet prof01")
    print("nom: ", prof01.get_name(),"/ prenom: ", prof01.get_lastName(), "/ craie: ", prof01.get_craie(), "/ sexe: ", prof01.get_sexe())
    print("On affiche à nouveau les attributs de l'objet prof02")
    print("nom: ", prof02.get_name(),"/ prenom: ", prof02.get_lastName(), "/ craie: ", prof02.get_craie(), "/ sexe: ", prof02.get_sexe())


if not __name__ in __name__ == "__main__":
    print("MDR LA VIE C'EST COMME LE SOLEIL CA VA DISPARAITRE")
