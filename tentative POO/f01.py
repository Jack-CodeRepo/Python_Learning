
# from model.cls01 import teacher

from model import cls01

if __name__ in __name__ == "__main__":
    prof01 = cls01.teacher("StreetCred", "Bobby", 10, "ambigu")
    print("premier professeur créé (attention il est armé)")
    print("nom: ", prof01.get_name(),"/ prenom: ", prof01.get_lastName(), "/ craie: ", prof01.get_craie(), "/ sexe: ", prof01.get_sexe())
    print()
    print("second professeur créé (attention il est naze, il n'a même pas de craie)")
    prof02 = cls01.teacher("Pondbeef","Jack", 0, "Dame")
    print("nom: ", prof02.get_name(), "/ prenom: ", prof02.get_lastName(), "/ craie: ", prof02.get_craie(), "/ sexe: ", prof02.get_sexe())
    print(prof02.get_lastName()," s'exclame \"VIE DE MERDE\"")

if not __name__ in __name__ == "__main__":
    print("MDR LA VIE C'EST COMME LE SOLEIL CA VA DISPARAITRE")
