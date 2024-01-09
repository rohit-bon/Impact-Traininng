class test():
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a,self.b)
    def update(self):
        self.a=self.a+10
        self.b=self.b+20

# Object 1
t1=test()
t1.insert()
t1.display()
t1.update()
t1.display()

# Object 2
t2 = test()
t2.insert()
t2.display()


# o/p:
# 1000 2000
# 1010 2020
# 1000 2000