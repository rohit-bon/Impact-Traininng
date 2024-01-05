l = lambda x, y: (x + y, x - y, x * y, x / y)
a,s,m,d = l(15,10)
print(f"Addition: {a}")
print(f"Subtraction: {s}")
print(f"Multiplication: {m}")
print(f"Division: {d}")



def op(a,b,s):
    r=s(a,b)
    return r
s1=op(10,5,lambda a,b:a+b)
s2=op(10,5,lambda a,b:a-b)
s3=op(10,5,lambda a,b:a*b)
s4=op(10,5,lambda a,b:a/b)
print(s1,s2,s3,s4)

# o/p:
# Addition: 25
# Subtraction: 5
# Multiplication: 150
# Division: 1.5
# 15 5 50 2.0