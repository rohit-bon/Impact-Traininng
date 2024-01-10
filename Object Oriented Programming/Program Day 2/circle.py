import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        ar = math.pi * self.radius**2
        print(ar)
    
    def perimeter(self):
        pr = math.pi * 2 * self.radius
        print(pr)
        
radius = int(input())
cir = Circle(radius)
cir.area()
cir.perimeter()


# o/p:
# 8
# 201.06192982974676
# 50.26548245743669