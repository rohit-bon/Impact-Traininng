class test():
    def insert(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a,self.b)
    def update(self):
        self.a=self.a+10
        self.b=self.b+20

# Object 1
t1=test()
t1.insert(10,20)
t1.display()
t1.update()
t1.display()

# Object 2
t2 = test()
t2.insert(40,50)
t2.display()


# o/p:
# 10 20
# 20 40
# 40 50