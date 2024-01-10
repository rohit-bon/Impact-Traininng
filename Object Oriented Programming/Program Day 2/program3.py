class Parent:
    def add(self,a,b):
        print(a+b)

class Child(Parent):
    def sub(self,a,b):
        print(a-b)
        
a=int(input())
b=int(input())
ch = Child()
ch.add(a,b)
ch.sub(a,b)


# o/p:
# 20
# 10
# 30
# 10