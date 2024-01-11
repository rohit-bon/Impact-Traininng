# write a program to create employee class with name, id, salary and initialize the properties through constructor and return the values to main program without using static and non static methods.
class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def __str__(self):
        return self.name+ ' '+ str(self.id)+ ' '+ str(self.salary)
emp = Employee("Rohit", 101, 5000)
print(emp)


# o/p:
# Rohit 101 5000