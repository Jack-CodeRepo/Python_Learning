# -*- coding: utf-8 -*-

def addition():
    a = input("saisissez le nombre de la table:")
        = input("saisissez le nombre multiplcateur maximum:")
    c = 0
    b = b+1
    while b != c:
        print a, "+ ", c, "= ", a + c
        c = c+1

def multiplication():
    a = input("saisissez le nombre nombre de la table:")
    b = input("saisissez le nombre maximum multiplicateur:")
    c = 0

    b = b+1
    while b != c:
        print a, "x ", c, "= ", a * c
        c = c+1



appel = 0
while appel != "lol":
    appel = input("Quelle fonction appeller (1_addition 2_multiplication 3_arreter):")
    if appel == "addition" or appel == 1:
        addition()
    elif appel == "multiplication"  or  appel == 2:
        multiplication()
    elif appel == "arreter"  or  appel == 3:
        exit()
