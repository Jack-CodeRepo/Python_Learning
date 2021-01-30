#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================

# ==================================================================================================
# DOCUMENTATION
# ==================================================================================================
"""Chmod Calculator.

    The <perm> argument must start with a 'r' since docopt do manage argument starting with "-" or "--"

    Usage:
        chmod_calc.py <perm>
        chmod_calc.py (-h | --help)         Show help page
        chmod_calc.py (-h | --version)      Show version

    examples:
        chmod_calc.py r-xr-xrwx returns 557
        chmod_calc.py rwxr-x--- returns 750

    Options:
        -h --help         Show this screen.
        -v --version      Show version.
"""



# ==================================================================================================
# IMPORTS
# ==================================================================================================

import sys
from docopt import docopt



# ==================================================================================================
# VARIABLES
# ==================================================================================================

argument = docopt(__doc__, version="alpha 1.0")
perm_arg = argument.get("<perm>")


r = 4
w = 2
x = 1



# ==================================================================================================
# FONCTIONS
# ==================================================================================================

def fnc_calc(perm):
    """Calcule les droits octal à partir des syboles r w x.

    Args:
        perm (str): la chaine de character indiuant les droits (ex: r-x-w---x)

    Returns:
        str: la valeur octale des droits
    """
    resList = []
    resInt = int()
    resStr = str()

    for i, l in enumerate(perm):

        if l == "r":
            resInt += r
        elif l == "w":
            resInt += w
        elif l == "x":
            resInt += x
        else:
            resInt += 0

        if i == 2 or i == 5 or i ==8:
            resList.append(str(resInt))
            resInt = 0
            continue

    resStr = "".join(resList)

    return resStr



# ==================================================================================================
# SCRIPT
# ==================================================================================================




if perm_arg:
    print(fnc_calc(perm_arg))




