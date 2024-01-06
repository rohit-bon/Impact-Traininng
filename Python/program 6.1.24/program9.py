s=[]
for i in range(3):
    r=[]
    for j in range(3):
        val = int(input())
        r.append(val)
    s.append(r)
    
print(s)

# o/p:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


l=[[int(input()) for i in range(3)] for j in range(3)]
print(l)
# o/p:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]