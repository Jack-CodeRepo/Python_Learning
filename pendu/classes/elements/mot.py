# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   CLASSES
# ==================================================================================================




class class_mot():
    def __init__(self, name=None, tentative=None):
        self.name = name
        self.tentative = tentative

    def get_name(self):
        return self.name

    def get_tentative(self):
        return self.tentative

    def set_name(self, value):
        self.name = value

    def set_tentative(self, value):
        self.tentative = value

    def lower_tentative(self, value):
        self.tentative = self.get_tentative() - value