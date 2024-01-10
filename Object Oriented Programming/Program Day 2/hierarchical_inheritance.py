class Student:
    def insert(self):
        self.name = input("Enter Name: ")
        self.id = int(input("Enter ID: "))
        self.add = input("Enter Address: ")
        
class DS(Student):
    def __init__(self):
        self.s1 = input("Enter Subject1: ")
        self.s2 = input("Enter Subject2: ")
    def display(self):
        self.insert()
        print(self.name,self.id,self.add,self.s1,self.s2)
        
class ML(Student):
    def __init__(self):
        self.s1 = input("Enter Subject1: ")
        self.s2 = input("Enter Subject2: ")
    def display(self):
        self.insert()
        print(self.name,self.id,self.add,self.s1,self.s2)
        
d1 = DS()
d1.display()

m1 = ML()
m1.display()


# o//p:
# Enter Subject1: ds1
# Enter Subject2: ds2
# Enter Name: Rohit
# Enter ID: 11
# Enter Address: Nagpur
# Rohit 11 Nagpur ds1 ds2
# Enter Subject1: ml1
# Enter Subject2: ml2
# Enter Name: Rohit
# Enter ID: 11
# Enter Address: Nagpur
# Rohit 11 Nagpur ml1 ml2