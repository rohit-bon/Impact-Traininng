n = int(input())
i = n
while i>0:
    j = i
    while j <= n:
        print(j,end=' ')
        j+=1
    print()
    i-=1
    
# o/p:
# 6 
# 5 6
# 4 5 6
# 3 4 5 6
# 2 3 4 5 6
# 1 2 3 4 5 6