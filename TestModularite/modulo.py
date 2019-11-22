# -*- coding: utf-8 -*-

# from test import *

from testPckg import test


appel = -1

while appel == -1:
    appel = input("Quelle fonction appeller (1_addition 2_multiplication 3_arreter):")
    if appel == "addition" or appel == 1:
        test.addition()
    elif appel == "multiplication"  or  appel == 2:
        test.multiplication()
    elif appel == "arreter"  or  appel == 3:
        exit()
