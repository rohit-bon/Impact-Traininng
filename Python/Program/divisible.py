# write a program to read a number from the user and check  whether it is divisible by 3 and 5 or not.
num=int(input("Enter a Number: "))
if num % 3 == 0:
    if num % 5 == 0:
        print(f"{num} is divisible by 3 and 5.")
    else:
        print(f"{num} is divisible by 3.")
else:
    if num  % 5 == 0:
        print(f"{num} is divisible by 5.")
    else:
        print(f"{num} is not divisible by 3 and 5.")
