# with filter and without lambda 
def even(n):
    return n%2 == 0
l=list(range(10,31))
r=list(filter(even,l))
print(r)

# with filter and with lambda 
l=list(range(10,31))
r=list(filter(lambda x:x%2 == 0,l))
print(r)

# with filter and without lambda 
def positive(n):
    return n>0
l=list(range(-5,6))
r=list(filter(positive,l))
print(r)

# with filter and with lambda 
l=list(range(-5,6))
r=list(filter(lambda x:x<0,l))
print(r)


l=["abc","ABC","xyz","WRT"]
r=list(filter(lambda x:x.isupper(),l))
print(r)


# o/p:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# [1, 2, 3, 4, 5]
# [-5, -4, -3, -2, -1]
# ['ABC', 'WRT']