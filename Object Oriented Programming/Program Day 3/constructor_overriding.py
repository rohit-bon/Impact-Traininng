class x:
    def __init__(self):
        print("Constructor of X")
class y(x):
    def __init__(self):
        print("Constructor of Y")
y_obj = y()

# o/p:
# Constructor of Y


class x:
    def __init__(self):
        print("Constructor of X")
class y(x):
    def __init__(self):
        print("Constructor of Y")
        super().__init__()
y_obj = y()

# o/p:
# Constructor of Y
# Constructor of X


class x:
    def __init__(self):
        print("Constructor of X")
class y(x):
    pass    
y_obj = y()

# o/p:
# Constructor of X

class x:
    def __init__(self,a):
        self.a = a
        print(self.a*self.a)
class y(x):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__(self.a)
        print(self.a+self.b)
y_obj = y(20,10)

# o/p:
# 400
# 30

class x:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a, self.b)
class y(x):
    def __init__(self, a):
        self.a = a
        print(self.a * self.a)
        super().__init__(10, 5)
y_obj = y(20)

# o/p:
# 400
# 10 5