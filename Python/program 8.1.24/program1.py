print("begin")
try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError):
    print("Input should be Integer")
print("end")


# o/p:
# begin
# 10
# abc
# Input should be Integer
# end

print("begin")
try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError):
    print("Input should be Integer")
except(ZeroDivisionError):
    print("Second Input should not be Zeero")
print("end")


# o/p:
# begin
# 10
# 0
# Second Input should not be Zeero
# end

print("begin")
try:
    a=int(input())
    b=int(input())
    print(a/b)
except(ValueError):
    print("Input should be Integer")
except(ZeroDivisionError):
    print("Second Input should not be Zeero")
finally:
    print("I am Finally Block")
print("end")

# o/p;
# begin
# 10
# abc
# Input should be Integer
# I am Finally Block
# end

# begin
# 10
# 0
# Second Input should not be Zeero
# I am Finally Block
# end

# begin
# 10
# 2
# 5.0
# I am Finally Block
# end