class x:
    def m1(self):
        print("I am m1")
    
x1 = x()
p = x1.__str__()
print(p)
x1.m1()

# o/p:
# <__main__.x object at 0x000002577A6C5730>
# I am m1
