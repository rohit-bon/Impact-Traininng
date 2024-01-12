from abc import *
class RBI(ABC):
    def min_balance(self):
        pass
    def RI(self):
        print("RI is 6.5%")

class SBI(RBI):
    def min_balance(self):
        print("Min Balance is 2k")

class HDFC(RBI):
    def min_balance(self):
        print("Min Balance is 0k")

class ICICI(RBI):
    def min_balance(self):
        print("Min Balance is 1k")
        
bank = input("Enter class / Bank name: ")
obj = globals() [bank]
obj1 = obj()
obj1.min_balance()
obj1.RI()


# o/p:
# Enter class / Bank name: SBI
# Min Balance is 2k
# RI is 6.5%


# Enter class / Bank name: HDFC
# Min Balance is 0k
# RI is 6.5%