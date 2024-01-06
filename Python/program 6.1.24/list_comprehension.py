l=[]
for i in range(1,11):
    l.append(i)
print(l)

l=[i for i in range(1,11)]
print(l)

l=[i for i in range(1,21) if (i%2==0)]
print(*l)

# o/p:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2 4 6 8 10 12 14 16 18 20