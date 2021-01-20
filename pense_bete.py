#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================


# ==================================================================================================
#   DICT
# ==================================================================================================

dico = {
    "key01": "value01",
    "key02": "value02",
    "key03": "value03",
    "keyEtc": "valueEtc",
}

dictVide = {}

# ==================================================================================================
#   LIST
# ==================================================================================================

ma_liste = [
    "elem01", "elem02", "elem03",
    "elem04", "elem05", "elem06",
    "elemEtc",
]

ma_listVide = []

# ajoute un element dans une liste
# ma_liste.append(element)

# ajoute un element dans une liste
# ma_liste.extend(element01, element02, element03, elementEtc)

# inserer un element à un index spécifique
# ma_liste.insert(index, element)

# enlever le premier element de la liste
# ma_liste.remove(element)

# enleve l'index et renvoi l'element de l'index spécifié
# si il n'y a pas d'index, enleve le dernier index et renvoi l'element du dernier index
# ma_liste.pop(index)

# enleve le premier index et renvoi l'element du premier index
# ma_liste.popleft()

# renvois l'index du premier element trouvé
# ma_liste.index(elem_a_trouver)

# Renvoie le nombre d’éléments dans la liste.
# ma_liste.count(elem_a_trouver)


# ==================================================================================================
#   Classes Sans Property
# ==================================================================================================

class my_class_de_qui_heriter:
    # constructeur de l'objet
    def __init__(self, atr01, atr02, atr03):
        self.atr01 = str(atr01)
        self.atr02 = str(atr02)
        self.atr03 = str(atr03)
    
    # fonction getter
    def get_atr01(self):
        return self.atr01

    def get_atr02(self):
        return self.atr02

    def get_atr03(self):
        return self.atr03



class my_class_qui_herite(my_class_de_qui_heriter):

    # dans le constructeur, on place tout les attributs nécessaires pour la classe my_class_qui_herite et my_class_de_qui_heriter
    def __init__(self, atr01, atr02, atr03, lol01, lol02):
        super().__init__(atr01, atr02, atr03)
        self.lol01 = lol01
        self.lol02 = lol02






# ==================================================================================================
#   Classes Avec Property
# ==================================================================================================

class my_classProp_de_qui_heriter:
    def __init__(self, atr01, atr02, atr03):
        self.__atr01 = str(atr01)
        self.__atr02 = str(atr02)
        self.__atr03 = str(atr03)

    @property
    def atr01(self):
        return self.__atr01

    @atr01.setter
    def atr01(self, value):
        self.__atr01 = value

    @property
    def atr02(self):
        return self.__atr02

    @atr02.setter
    def atr02(self, value):
        self.__atr02 = value

    @property
    def atr03(self):
        return self.__atr03

    @atr03.setter
    def atr03(self, value):
        self.__atr03 = value



# la classe "my_classProp_qui_herite" hérite des attributs et méthodes de la class "my_classProp_de_qui_heriter"
class my_classProp_qui_herite(my_classProp_de_qui_heriter):
    def __init__(self, atr01, atr02, atr03, lol01, lol02):
        super().__init__(atr01, atr02, atr03)
        self.__lol01 = int(lol01)
        self.__lol02 = int(lol02)

    @property
    def lol01(self):
        return self.__lol01

    @property
    def lol02(self):
        return self.__lol02

    # setter de lol01
    @lol01.setter
    def lol01(self, value):
        self.__lol01 = value

    # setter de lol02
    @lol02.setter
    def lol02(self, value):
        self.__lol02 = value