import re

mob = input("Enter Mobile number: ")
check_mob = re.fullmatch("[6-9]\d{9}",mob)
if check_mob:
    print("Valid Mobile Number")
else:
    print("Not Valid Numberr")