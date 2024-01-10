class Student:
    def __init__(self,name,roll,sub1,sub2,sub3):
        self.name = name
        self.roll = roll
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def display(self):
        result = (self.sub1+self.sub2+self.sub3)/3
        if self.sub1>35 and self.sub2>35 and self.sub3>35:
            print(self.name, self.roll, result)
        else:
            print("You are Failed.")

class FindResult:
    def showResult(studnet_obj):
        studnet_obj.display()
        
std = Student("Rohit",101,89,93,91)
FindResult.showResult(std)


# o/p:
# Rohit 101 91.0