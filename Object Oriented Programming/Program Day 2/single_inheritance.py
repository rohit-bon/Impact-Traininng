class x:
    def m1(self):
        print("I am m1")
class y(x):
    def m2(self):
        print("I am m2")
print(x.__bases__)
print(y.__bases__)
y1 = y()
y1.m1()
y1.m2()
p=y1.__hash__()
print(p)


# o/p:
# (<class 'object'>,)
# (<class '__main__.x'>,)
# I am m1
# I am m2
# 128973854340