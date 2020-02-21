
class person:
    def __init__(self, name, lastName,sexe):
        self.name = str(name)
        self.lastName = str(lastName)
        self.sexe = str(sexe)
    
    def get_name(self):
        return self.name

    def get_lastName(self):
        return self.lastName

    def get_sexe(self):
        return self.sexe


class teacher(person):
    def __init__(self, nom, prenom, craie, sexe):
        super().__init__(nom, prenom, sexe)
        self.craie = craie

    def get_craie(self):
        return self.craie


