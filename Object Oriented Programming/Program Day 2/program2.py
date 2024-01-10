class X:
    a=1000
    def __init__(self):
        self.b = 2000
    def m1(self):
        print("I am m1.")
class Y:
    c=3000
    def __init__(self):
        self.d = 4000
    def m2():
        print("I am m2")
    def display(self):
        print(Y.c)
        print(self.d)
        Y.m2()
        x1 = X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        
y1 = Y()
y1.display()


# o/p:
# 3000
# 4000
# I am m2
# 1000
# 2000
# I am m1.