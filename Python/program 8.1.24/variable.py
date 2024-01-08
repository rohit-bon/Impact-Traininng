def f1():
    a = 10
    b = 20
    print(a,b)
    

def f2():
    c,d = 30,40
    print(c,d)
    # print(a)


f1()
f2()


# o/p:
# 10 20
# 30 40
# Traceback (most recent call last):
#   File "d:\Impact Traininng\Python\program 8.1.24\variable.py", line 14, in <module>
#     f2()
#   File "d:\Impact Traininng\Python\program 8.1.24\variable.py", line 10, in f2
#     print(a)


a=10
def m1():
    print(a)
m1()
a=a+10
print(a)
m1()


# o/p:
# 10
# 20
# 20


a=10
def m1():
    global a
    print(a)
    a+=10
    print(a)

m1()

# o/p:
# 10
# 20


a = 10
b = 20
c = 30
def m1(a):
    print(a+b+c)
m1(50)

# o/p:
# 100