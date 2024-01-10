class Employee:
    company_name = "Goldman Sachs"
    def __init__(self,name,id,address,salary):
        self.name = name
        self.id = id
        self.address = address
        self.salary = salary
    
    def display(self):
        print(Employee.company_name)
        print("Employee name:",self.name)
        print("Id:",self.id)
        print("Address:",self.address)
        print("Salary:",self.salary)
        
n = int(input("Enter number of Employees:"))
while(n>0):
    name = input("Enter Employee Name: ")
    id = input("Enter id: ")
    address = input("Enter Address: ")
    salary = input("Enter Salary: ")
    
    employee_obj = Employee(name,id,address,salary)
    employee_obj.display()
    print("************************************************")
    n-=1


# o/p:
# Enter number of Employees:2
# Enter Employee Name: Rohit
# Enter id: 101
# Enter Address: nagpur
# Enter Salary: 5000000
# Goldman Sachs
# Employee name: Rohit
# Id: 101
# Address: nagpur
# Salary: 5000000
# ************************************************
# Enter Employee Name: KArtik
# Enter id: 111
# Enter Address: nag
# Enter Salary: 3000000
# Goldman Sachs
# Employee name: KArtik
# Id: 111
# Address: nag
# Salary: 3000000
# ************************************************