#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk


# ==================================================================================================
#   CLASSES
# ==================================================================================================


class saisie(tk.Entry):
    def __init__(self, parent, xRow, yCol, width, cSpan, label=None):
        """
            Gere les zone de saisie

            :param parent: fenetre dans laquelle afficher le bouton
            :type parent: [type]
            :param xRow: coordonnée x (horizontal) de la zone de saisie
            :type xRow: int
            :param yCol: coordonnée y (vertical) de la zone de saisie
            :type yCol: int
            :param width: largeur de la zone de saisie
            :type width: int
            :param cSpan: nombre de column sur lequel la zone s'affiche
            :type cSpan: int
            :param label: nom de la zone saisie, positionne à gauche de la zone
            :type label: str, optional
        """
        
        tk.Entry.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.width = width
        self.cSpan = cSpan
        self.label = label

        # création zone de saisie (entry)
        self.saisie = tk.Entry(parent, width=self.width)
        self.saisie.grid(row=self.xRow, column=self.yCol+1, columnspan=self.cSpan, sticky="nsew")

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

    def forget_saisie(self):
        self.saisie.grid_forget()

    def forget_saisie_label(self):
        self.saisie_label.grid_forget()
