class test:
    a=1000
    b=2000
    def display(self):
        print(test.a,test.b)
    def update(self):
        test.a = test.a+10
        test.b = test.b+20

# for object 1
t1 = test()
t1.display()
t1.update()
t1.display()


# for object 2
t2 = test()
t2.display()
t2.update()
t2.display()


# o/p:
# 1000 2000
# 1010 2020
# 1010 2020
# 1020 2040