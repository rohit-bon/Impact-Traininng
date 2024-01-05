def sq(n):
    return n*n
l=[1,2,3,4,5]
r=tuple(map(sq,l))
print(r)

l=[1,2,3,4,5]
r=tuple(map(lambda x:x*x,l))
print(r)

s=["abc","xyz","rqt"]
r=tuple(map(lambda x:x.upper(),s))
print(r)


# o/p:
# (1, 4, 9, 16, 25)
# (1, 4, 9, 16, 25)
# ('ABC', 'XYZ', 'RQT')