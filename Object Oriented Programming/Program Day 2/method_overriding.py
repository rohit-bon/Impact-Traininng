class x:
    def m1(self):
        print("I am m1 of X")
    def m2(self):
        print("I am m2 of X")
class y(x):
    def m2(self):
        print("I am m2 of Y")
    def m3(self):
        print("I am m3 of Y")
class z(x):
    def m1(self):
        print("I am m1 of Z")
    def m4(self):
        print("I am m4 of Z")
        
y1 = y()
y1.m2()
y1.m1()
y1.m3()
z1=z()
z1.m1()
z1.m2()
z1.m4()


# o/p:
# I am m2 of Y
# I am m1 of X
# I am m3 of Y
# I am m1 of Z
# I am m2 of X
# I am m4 of Z