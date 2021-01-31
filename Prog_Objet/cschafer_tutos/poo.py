#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================



# ==================================================================================================
#   DICT
# ==================================================================================================



# ==================================================================================================
#   LISTS
# ==================================================================================================



# ==================================================================================================
#   FONCTIONS
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class employee:

    aug_tx = 1.05

    def __init__(self, prenom, nom, paye):
        self.prenom = prenom
        self.nom = nom
        self.paye = int(paye)


    def mem_hex_adress(self):
        return hex(id(self))


    def mem_adress(self):
        return id(self)


    def aug_paye(self):
        self.paye = int(self.paye * self.aug_tx)


    @property
    def fullname(self):
        return "{} {}".format(self.prenom, self.nom)


    @fullname.setter
    def fullname(self, name):
        self.prenom, self.nom = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.prenom = None
        self.nom = None





    def email(self):
        return "{}.{}@company.com".format(self.prenom, self.nom).lower()





    @classmethod
    def set_aug_tx(cls, tx):
        cls.aug_tx = tx


    @classmethod
    def from_string(cls, string):
        prenom, nom, paye = string.split("-")
        return cls(prenom, nom, paye)


    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email())




class developer(employee):
    aug_tx = 1.2

    def __init__(self, prenom, nom, paye, language):
        super().__init__(prenom, nom, paye)
        self.language = language




class manager(employee):
    aug_tx = 1.5

    def __init__(self, prenom, nom, paye, emp=None):
        super().__init__(prenom, nom, paye)
        if emp == None:
            self.emp = []
        else:
            self.emp = emp


    def add_emp(self, emp):
        if emp not in self.emp:
            self.emp.append(emp)



    def remove_emp(self, emp):
        if emp in self.emp:
            self.emp.remove(emp)


    def liste_emp(self):
        for e in self.emp:
            print("List of managed employees:")
            print(e.fullname)



# ==================================================================================================
#   SCRIPT
# ==================================================================================================


empl_1 = developer("Jacques", "Marboeuf", "22000", "bash")
empl_2 = manager("Corey", "Schafer", "40000")


print(empl_1.prenom, empl_1.nom, empl_1.paye)
print(empl_1.email())

empl_1.fullname = 'Tiny Tim'
print(empl_1.prenom, empl_1.nom)
print(empl_1.prenom, empl_1.nom, empl_1.paye)


del empl_1.fullname
print(empl_1.prenom, empl_1.nom)
print(empl_1.prenom, empl_1.nom, empl_1.paye)