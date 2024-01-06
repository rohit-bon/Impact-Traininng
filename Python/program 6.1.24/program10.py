n=int(input())
l=list(map(int,input().split()))[:n]
print(l)
l.sort()
print("Max:",l[-1])
c = l.count(l[-1])
print("2nd Max:",l[-(c+1)])
print("Min:",l[0])
c = l.count(l[0])
print("2nd Min:",l[c])

# o/p:
# 6
# 1 1 2 3 6 6
# [1, 1, 2, 3, 6, 6]
# Max: 6
# 2nd Max: 3
# Min: 1
# 2nd Min: 2