from functools import reduce
s=[1,2,3,4,5]
r=reduce(lambda a,b:a+b,s)
print(r)


s=[1,2,3,4,5]
r=reduce(lambda a,b:a*b,s)
print(r)

d=[12,3,15,9,17,21,25,1]
mi = reduce(lambda a,b:a if a<b else b,d)
print(mi)
ma = reduce(lambda a,b:a if a>b else b,d)
print(ma)

# o/p:
# 15
# 120
# 1
# 25