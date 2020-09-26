# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

import tkinter as tk


# ==================================================================================================
#   CLASSES
# ==================================================================================================


class bouton(tk.Button):
    def __init__(self, parent, xRow, yCol, titre, cmd):
        """
            Gere la zone d'affichage

            :param parent: fenetre dans laquelle afficher le bouton
            :type parent: 
            :param xRow: coordonnée x (horizontal) de la zone d'affichage
            :type xRow: int
            :param yCol: coordonnée y (vertical) de la zone d'affichage
            :type yCol: int
            :param titre: nom du bouton
            :type titre: str
            :param cmd: fonction à associer au bouton
            :type cmd: 
        """

        tk.Button.__init__(self)
        self.xRow = xRow
        self.yCol = yCol

        self.bouton = tk.Button(parent, text=titre, height=1, width=15, command=cmd)
        self.bouton.grid(row=self.xRow, column=self.yCol, sticky ="nsew")
