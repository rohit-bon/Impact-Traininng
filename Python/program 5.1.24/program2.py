num = int(input())
li=[]
while(num>0):
    li.append(num%2)
    num = num // 2
print(*li)


# o/p:
# 10
# 0 1 0 1