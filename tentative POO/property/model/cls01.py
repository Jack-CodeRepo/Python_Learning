
class person:
    def __init__(self, name, lastName, sexe):
        self.__name = str(name)
        self.__lastName = str(lastName)
        self.__sexe = str(sexe)

    @property
    def name(self):
        return self.__name

    @property
    def lastName(self):
        return self.__lastName

    @property
    def sexe(self):
        return self.__sexe



# la classe "teacher" hérite des attributs et méthodes de la class "person"
class teacher(person):
    def __init__(self, nom, prenom, craie, sexe):
        super().__init__(nom, prenom, sexe)
        self.__craie = int(craie)

    @property
    def craie(self):
        return self.__craie

    @craie.setter
    def craie(self, craie):
        self.__craie = craie