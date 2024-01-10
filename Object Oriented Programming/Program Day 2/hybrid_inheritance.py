class V:
    def v(self):
        print("In v of V")
class W(V):
    def m(self):
        self.v()
        print("In m of W")
class X(W):
    def m1(self):
        self.m()
        print("In m1 of X")
class Y(V):
    def m1(self):
        self.v()
        print("In m2 of Y")
class Z(X,Y):
    def m3(self):
        self.m1()
        print("In m3 Of Z")
z1=Z()
z1.m3()

# o/p:
# In v of V
# In m of W
# In m1 of X
# In m3 Of Z