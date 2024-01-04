s=input()
r=set(s)
l=list(r)
l.sort()
for i in l:
    print(i," = ",s.count(i))

# o/p:
# 2334
# 2  =  1
# 3  =  2
# 4  =  1