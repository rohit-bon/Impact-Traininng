# Public
class Employee:
    def __init__(self,name,id1,salary,dept):
        self.name = name
        self.id1 = id1
        self.salary = salary
        self.dept = dept
    
    def display(self):
        print(emp_obj.name)
        print(emp_obj.id1)
        print(emp_obj.salary)
        print(emp_obj.dept)

emp_obj = Employee("Rohit",123,100000,"IT")
emp_obj.display()
print(emp_obj.name)
print(emp_obj.id1)
print(emp_obj.salary)
print(emp_obj.dept)

# o/p:
# Rohit
# 123
# 100000
# IT
# Rohit
# 123
# 100000
# IT

# Protected
class Employee:
    def __init__(self,name,id1,salary,dept):
        self._name= name
        self._id1 = id1
        self._salary = salary
        self._dept = dept
    
    def _display(self):
        print("Name: ",self._name)
        print("ID: ",self._id1)


class Geeks(Employee):
    def __init__(self, name, id1, salary, dept):
        super().__init__(name, id1, salary, dept)
    def display(self):
        self._display()
        print("Salary",self._salary)
        print("Department",self._dept)
        
geeks_obj = Geeks("Rohit",123,100000,"CSE")
geeks_obj.display()


# o/p:
# Name:  Rohit
# ID:  123
# Salary 100000
# Department CSE

#Private

class Employee:
    __cname = "Parul Univeristy"
    
    def __init__(self,name,id1,salary,dept):
        self.__name = name
        self.__id1 = id1
        self.__salary = salary
        self.__dept = dept
    
    def __display(self):
        print("College Name: ",Employee.__cname)
        print("Name: ",self.__name)
        print("ID: ",self.__id1)
        print("Department: ",self.__dept)
        print("Salary: ",self.__salary)
    
    def display(self):
        self.__display()

emp_obj = Employee("Rohit",123,100000,"CSE")
emp_obj.display()

# o/p:
# College Name:  Parul Univeristy
# Name:  Rohit
# ID:  123
# Department:  CSE
# Salary:  100000