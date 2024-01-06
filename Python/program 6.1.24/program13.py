print("Begin: ")
a=int(input("Enter value od a:"))
b=int(input("Enter value od b:"))
try:
    c=a/b
    print("Result: ",c)
except(ZeroDivisionError):
    print("Not Divisible by zero")
print("End")


# o/p:
# Begin: 
# Enter value od a:10
# Enter value od b:0
# Not Divisible by zero
# End