l1=[[int(input()) for i in range(2)]for j in range(2)]
l2=[[int(input()) for i in range(2)]for j in range(2)]
l3=[]
for i in range(2):
    r=[]
    for j in range(2):
        s=l1[i][j]+l2[i][j]
        r.append(s)
    l3.append(r)
for i in l3:
    print(*i)
    
# o/p:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 6 8
# 10 12