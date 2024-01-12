from abc import *

class Test(ABC):
    def operation(self):
        pass

class Sub1(Test):
    def operation(self,a):
        self.a = a
        print(self.a * self.a)

class Sub2(Test):
    def operation(self,a):
        self.a = a
        print(self.a**3)

class Sub3(Test):
    def operation(self,a,b):
        self.a = a
        self.b = b 
        print(self.a+self.b)

sub1_obj = Sub1()
sub1_obj.operation(10)

sub2_obj = Sub2()
sub2_obj.operation(5)

sub3_obj = Sub3()
sub3_obj.operation(3,2)


# o/p:
# 100
# 125
# 5