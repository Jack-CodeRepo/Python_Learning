#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================




class class_mot():
    def __init__(self, name: str = "", tentative: int = None):
        """
            class gérant le mot en tant qu'objet

            :param name: valeure du mot, defaults to None
            :type name: str, optional
            :param tentative: nombre de tentative pour trouver le mot, defaults to None
            :type tentative: int, optional
        """
        
        self.name = name
        self.tentative = tentative

    def get_name(self):
        return self.name

    def get_tentative(self):
        return self.tentative

    def set_name(self, value):
        self.name = value

    def set_tentative(self, value):
        self.tentative = int(value)

    def lower_tentative(self, value):
        self.tentative = int(self.get_tentative()) - int(value)