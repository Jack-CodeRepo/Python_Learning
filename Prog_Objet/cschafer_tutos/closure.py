#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


def fonc_ext(txt):
    msg = txt

    def fonc_int():
        print(msg)
    
    return fonc_int


fonc_1 = fonc_ext("hey")
fonc_2 = fonc_ext("hay")

fonc_1()
fonc_2()
