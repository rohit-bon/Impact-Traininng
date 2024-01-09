import math
class area():
    def __init__(self,r):
        self.r = r
    
    def display(self):
        area = math.pi * self.r**2 
        print("Area is:",area)

ar = area(7)
ar.display()


# o/p:
# Area is: 153.93804002589985