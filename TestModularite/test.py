# -*- coding: utf-8 -*-

import time

def addition():
    a = int(input("saisissez le nombre de la table:"))
    b = int(input("saisissez le nombre maximum a additionner:"))
    c = 0
    b = b + 1
    while b != c:
        print(a, "+ ", c, "= ", a + c)
        time.sleep(0.25)
        c = c + 1

def multiplication():
    a = int(input("saisissez le nombre de la table:"))
    b = int(input("saisissez le nombre maximum a additionner:"))
    c = 0
    b = b + 1
    while b != c:
        print(a, "x ", c, "= ", a * c)
        time.sleep(0.25)
        c = c + 1


cnt = 0

while cnt == 0:
    appel = int(input("Quelle fonction appeller (1_addition 2_multiplication 3_arreter):"))
    if appel == 1:
        addition()
    elif appel == 2:
        multiplication()
    elif appel == 3:
        exit()
