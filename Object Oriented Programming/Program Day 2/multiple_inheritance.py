class x:
    def m1(self):
        print("I am m1 of X")
class y:
    def m1(self):
        print("I am m1 of Y")
class z(x,y):
    def m2(self):
        print("I am m2 of z")

z1 = z()
z1.m1()

# o/p:
# I am m1 of X