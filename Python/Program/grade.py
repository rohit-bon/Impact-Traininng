# write a program to read name of the student rollno and 3 subject marks, if student is pass calculate the grade of the student 
name = input("Enter your name: ")
roll = int(input("Roll number: "))
s1,s2,s3 = map(int, input("Enter marks of 3 subject: ").split(","))

print(f"Name: {name}\nRoll no: {roll}\nMarks of S1: {s1}\nMarks of S2: {s2}\nMarks of S3: {s3}")
if s1>35 and s2>35 and s3>35:
    total = s1+s2+s3
    average = total/3
    if average>90:
        print(f"{name} You Secured Grade A+")
    elif average>75:
        print(f"{name} You Secured Grade A")
    elif average>60:
        print(f"{name} You Secured Grade B")
    elif average>50:
        print(f"{name} You Secured Grade C")
    elif average>35:
        print(f"{name} You Passed")
    else:
        print(f"{name} You are failed")
else:
    print(f"{name} You are failed")