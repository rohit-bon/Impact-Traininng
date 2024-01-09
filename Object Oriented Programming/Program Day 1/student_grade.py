class Student():
    school_name = "My School"
    
    def __init__(self, name,roll,add):
        self.name = name
        self.roll = roll
        self.add = add
    
    def read_marks(self):
        self.sub1 = int(input("Marks of Subject1: "))
        self.sub2 = int(input("Marks of Subject2: "))
        self.sub3 = int(input("Marks of Subject3: "))
    
    def calculate_grade(self):
        print(self.school_name)
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Address:",self.add)
        print("Subject 1 Marks:",self.sub1)
        print("Subject 2 Marks:",self.sub2)
        print("Subject 3 Marks:",self.sub3)
        if self.sub1 <=35 or self.sub2 <=35 or self.sub3 <=35:
            print(self.name,"you are failed")
            grade=0
        else:
            grade = (self.sub1+self.sub2+self.sub3)/3
            print("Your Grade:",grade)
        if grade >= 75:
            print("Grade is A")
        elif grade >=60:
            print("Grade is B")
        elif grade >=50:
            print("Grade is C")


name = input("Enter Your Name: ")
roll = input("Enter your roll no: ")
add = input("Enter your address: ")
std = Student(name,roll,add)
std.read_marks()
std.calculate_grade()


# o/p:
# Enter Your Name: rohit
# Enter your roll no: 14
# Enter your address: nag
# Marks of Subject1: 20
# Marks of Subject2: 30
# Marks of Subject3: 40
# My School
# Name: rohit
# Roll: 14
# Address: nag
# Subject 1 Marks: 20
# Subject 2 Marks: 30
# Subject 3 Marks: 40
# rohit you are failed


# Enter Your Name: Rohit
# Enter your roll no: 15
# Enter your address: Nagpur
# Marks of Subject1: 70
# Marks of Subject2: 80
# Marks of Subject3: 90
# My School
# Name: Rohit
# Roll: 15
# Address: Nagpur
# Subject 1 Marks: 70
# Subject 2 Marks: 80
# Subject 3 Marks: 90
# Your Grade: 80.0
# Grade is A