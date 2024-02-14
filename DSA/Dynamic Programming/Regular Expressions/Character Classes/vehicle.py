import re

vehicle = input("Enter Vehicle Number ")
check_vehicle = re.fullmatch("[A-Z]{2}\d{2}[A-Z]\d{4}",vehicle)
if check_vehicle != None:
    print("Valid Number")
else:
    print("Not Valid")