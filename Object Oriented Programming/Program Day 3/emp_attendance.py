class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    def __mul__(self,other):
        return self.sal * other.days
class Attendance:
    def __init__(self,days):
        self.days = days
emp_obj = Employee("Rohit", 1000)
attend = Attendance(29)
print(emp_obj * attend)

# o/p:
# 29000: