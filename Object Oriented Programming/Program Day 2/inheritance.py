class X:
    a=1000
    def __init__(self):
        self.b = 2000
    def m1(self):
        print("I am m1")
class Y(X):
    c=3000
    def __init__(self):
        self.d = 4000
        super().__init__()
    def m2(self):
        print("I am m2")
    def display(self):
        print(X.a)
        print(self.b)
        self.m1()
        print(Y.c)
        self.m2()
        print(self.d)

y1 = Y()
y1.display()

# o/p:
# 1000
# 2000
# I am m1
# 3000
# I am m2
# 4000

print(y1.a,y1.b,y1.c,y1.d)
y1.m1()
y1.m2()


# o/p:
# 1000 2000 3000 4000
# I am m1
# I am m2