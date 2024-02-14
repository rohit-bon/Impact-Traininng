import re

mail = input("Enter mail id: ")
check_mail = re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$",mail)
if check_mail:
    print("Valid")
else:
    print("Invalid")
print(check_mail)
