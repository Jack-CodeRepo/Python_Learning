# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk


# ==================================================================================================
#   CLASSES
# ==================================================================================================


class saisie(tk.Entry):
    '''
        type: class
        Gere les zone de saisie

        Arguments:
        xRow: coordonnée x (horizontal) de la zone de saisie
        yCol: coordonnée y (vertical) de la zone de saisie
        label: nom de la zone saisie, positionne à gauche de la zone
    '''
    def __init__(self, parent, xRow, yCol, label=None):
        tk.Entry.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.label = label

        # création zone de saisie (entry)
        self.saisie = tk.Entry(parent, width=10)
        self.saisie.grid(row=self.xRow, column=self.yCol+1)

        # création du nom de la zone de saisie (label)
        self.saisie_label = tk.Label(parent, text=self.label)
        self.saisie_label.grid(row=self.xRow, column=self.yCol, sticky="nsew")


    def get_value(self):
        '''
            Méthode qui récupere la valeur rentrée
        '''
        a = self.saisie.get()
        if not a:
            return False
        else:
            return self.saisie.get()
