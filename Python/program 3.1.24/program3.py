e={
    "Name":"Rohit",
    "id":101,
    "Dept":"CSE",
    "Salary":250000
}

print(e)
print(e["Dept"])
d=e.get("Salary")
print(d)
e["Salary"]=350000
print(e)
e["Subject"]="Flutter"
print(e)
for i in e.keys():
    print(i)
for i in e.values():
    print(i)
for i,j in e.items():
    print(i,j)
for i in e.items():
    print(i)
for i in e.items():
    print(i[0], i[1])
r=sorted(list(e.keys()))
print(r)


# o/p:
# {'Name': 'Rohit', 'id': 101, 'Dept': 'CSE', 'Salary': 250000}
# CSE
# 250000
# {'Name': 'Rohit', 'id': 101, 'Dept': 'CSE', 'Salary': 350000}
# {'Name': 'Rohit', 'id': 101, 'Dept': 'CSE', 'Salary': 350000, 'Subject': 'Flutter'}
# Name
# id
# Dept
# Salary
# Subject
# Rohit
# 101
# CSE
# 350000
# Flutter
# Name Rohit
# id 101
# Dept CSE
# Salary 350000
# Subject Flutter
# ('Name', 'Rohit')
# ('id', 101)
# ('Dept', 'CSE')
# ('Salary', 350000)
# ('Subject', 'Flutter')
# Name Rohit
# id 101
# Dept CSE
# Salary 350000
# Subject Flutter
# ['Dept', 'Name', 'Salary', 'Subject', 'id']