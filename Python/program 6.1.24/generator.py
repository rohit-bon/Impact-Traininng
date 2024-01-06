def gen():
    yield 5
    yield 10
    yield 15
    yield 20
g1=gen()
r=next(g1)
r1=next(g1)
r2=next(g1)
r3=next(g1)
print(r,r1,r2,r3)

# o/p:
# 5 10 15 20

# --------------------------------------------------------------------------------------------------------------------------

def gen():
    l=[5,10,15,20]
    for i in l:
        yield i
g1=gen()
for i in g1:
    print(i)

# o/p:
# 5
# 10
# 15
# 20