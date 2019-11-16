# -*- coding: utf-8 -*-

def multiplication():

    nbTab = input("Saissisez le nombre de la table: ")
    nbMax = input("Saissisez le nombre maximum à multiplier: ")
    cnt = 0
    while nbMax != cnt:
        print(nbTab, "x", cnt, " = ", nbTab * cnt)
        cnt = cnt + 1
        break

multiplication()
