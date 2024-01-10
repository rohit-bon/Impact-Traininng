class person:
    def insert(self):
        self.name = "Rohit"
        self.add = "NGP"
class employee(person):
    def insert1(self):
        self.id = 101
class salaried_employee(employee):
    def __init__(self):
        self.sal = 50000
    def display(self):
        self.insert()
        self.insert1()
        print(self.name, self.id, self.add, self.sal)
        
emp1 = salaried_employee()
emp1.display()


# o/p:
# Rohit 101 NGP 50000