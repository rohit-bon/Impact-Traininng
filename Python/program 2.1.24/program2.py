li=list(map(int,input().split()))
print(li)

n=int(input())
li=list(map(int,input().split()))[:n]
print(li)

n=int(input())
r=[]
for i in range (n):
    val = int(input())
    r.append(val)
print(r)

# o/p:
# 1 2 3 4 5
# [1, 2, 3, 4, 5]
# 4
# 1 2 3 4
# [1, 2, 3, 4]
# 4
# 1  
# 2
# 3
# 4
# [1, 2, 3, 4]