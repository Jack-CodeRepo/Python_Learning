# -*- coding: utf-8 -*-
# ===================================================================================================


# ===================================================================================================
#   IMPORT
# ===================================================================================================

# ===================================================================================================
#   CLASS MONEY
# ===================================================================================================

class money:
    def __init__(self, amnt):
        self.amnt = int(amnt)

    def get_amnt(self):
        return self.amnt
    
    def amnt_increase(self, incr):
        self.amnt = self.amnt + incr
        return self.amnt

    def amnt_decrease(self, decr):
        self.amnt = self.amnt - decr
        return self.amnt

