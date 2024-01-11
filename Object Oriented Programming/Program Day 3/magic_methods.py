class bx:
    def __init__(self,p):
        self.p = p
    def __add__(self,other):
        d = self.p+other.p
        return d
class by:
    def __init__(self,p):
        self.p = p
b1 = bx(200)
b2 = by(100)
print(b1+b2)

# o/p:
# 300

class bx:
    def __init__(self,p):
        self.p = p
    def __add__(self,other):
        d = self.p+other.p
        return d
class by:
    def __init__(self,p):
        self.p = p
b1 = bx(200)
b2 = by(100)
c = b1.__add__(b2)
print(c)

# o/p:
# 300