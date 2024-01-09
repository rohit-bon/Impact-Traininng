class test():
    a=1000
    b=2000
    def display(self):
        print(test.a,test.b)
    def update(self):
        test.a=test.a+10
        test.b=test.b+20
print(test.a,test.b)
t1 = test()
t1.display()
print(t1.a,t1.b)


# o/p:
# 1000 2000
# 1000 2000
# 1000 2000