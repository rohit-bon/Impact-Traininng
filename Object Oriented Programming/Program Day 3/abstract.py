from abc import *

class RBI(ABC):
    def min_bal(self):
        pass
    def RI(self):
        print("RI is 6.5%")
class SBI(RBI):
    def min_bal(self):
        print("Min bal is 2k.")
class HDFC(RBI):
    def min_bal(self):
        print("Min bal is 0k.")
class BOI(RBI):
    def min_bal(self):
        print("Min bal is 1k")
        
s1 = SBI()
s1.min_bal()
s1.RI()

s2 = HDFC()
s2.min_bal()
s2.RI()

# o/p:
# Min bal is 2k.
# RI is 6.5%
# Min bal is 0k.
# RI is 6.5%