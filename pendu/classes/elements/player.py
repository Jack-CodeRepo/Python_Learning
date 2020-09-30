# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================



class class_player():
    def __init__(self, name: str = None, score: int = None):
        """
        class gérant le joueur en tant qu'objet


        :param name: nom du joueur, defaults to None
        :type name: str, optional
        :param score: score du joueur, defaults to None
        :type score: int, optional
        """
        
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_name(self, value):
        self.name = value

    def set_score(self, value):
        self.score = value

    def lower_score(self, value):
        self.score = int(self.get_score()) - int(value)

    def increase_score(self, value):
        self.score = int(self.get_score()) + int(value)