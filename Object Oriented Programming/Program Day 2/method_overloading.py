class x:
    def m1(self):
        print("No Parameter m1")
    def m1(self,a):
        print("1 Parameter m1")
    def m1(self,a,b):
        print("2 Parameter m1")

x1 = x()
x1.m1(10,20)

# o/p:
# 2 Parameter m1

x1.m1(10)

# o/p:
#     x1.m1(10)
# TypeError: x.m1() missing 1 required positional argument: 'b'