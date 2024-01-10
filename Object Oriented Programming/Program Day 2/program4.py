# class x:
#     def m1(self):
#         print("M1 of X")
#     def __str__(self):
#         return "python"
    
# x1=x()
# p=x1.__str__()
# print(p)

# o/p:
# python

class x:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    
x1=x("Rohit")
print(x1)

# o/p:
# Rohit