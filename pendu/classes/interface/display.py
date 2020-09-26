
# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk


# ==================================================================================================
#   CLASSES
# ==================================================================================================




class display(tk.Text):
    def __init__(self, parent, xRow, yCol, w, h, rSpan):
        """
             Gere la zone d'affichage
            :param parent: fenetre dans laquelle afficher le bouton
            :type parent: [type]
            :param xRow: coordonnée x (horizontal) de la zone d'affichage
            :type xRow: int
            :param yCol: coordonnée y (vertical) de la zone d'affichage
            :type yCol: int
            :param w: largeur de la zone d'affichage
            :type w: int
            :param h: hauteur de la zone d'affichage
            :type h: int
            :param rSpan: nombre de row sur lequel la zone s'affiche
            :type rSpan: int
        """

        tk.Text.__init__(self)
        self.xRow = xRow
        self.yCol = yCol
        self.width = w
        self.height = h
        self.rowspan = rSpan

        self.boite_texte = tk.Text(parent, width=self.width, height=self.height, state=tk.DISABLED)
        self.boite_texte.grid(row=self.xRow, column=self.yCol, rowspan=self.rowspan, sticky="nsew")


    def get_text(self):
        return self.boite_texte
