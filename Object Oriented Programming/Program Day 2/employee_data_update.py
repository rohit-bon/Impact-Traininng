class Employee:
    company_name = "Sampurv"
    def emp_data(self, name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary

class Test:
    def update_salary(self,emp_obj):
        emp_obj.salary += 5000
        print(emp_obj.salary)

emp_object = Employee()
emp_object.emp_data("Rohit",101,10000)

test_obj = Test()
test_obj.update_salary(emp_object)

# o/p:
# 15000

class Emp:
    def __init__(self,name,id,sal):
        self.name = name
        self.id = id
        self.sal = sal
    
    def display(self):
        print(self.name,self.id,self.sal)
        
class Tes:
    def update(e):
        e.sal = 50000
        e.display()

e1 = Emp("Rohit",101,40000)
e1.display()
Tes.update(e1)


# o/p:
# Rohit 101 40000
# Rohit 101 50000