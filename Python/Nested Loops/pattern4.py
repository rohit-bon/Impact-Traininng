i=1
while i <= 5:
    j = i
    while j <= 5:
        print(j, end = ' ')
        j+=1
    print()
    i+=1
i = 6
while i>0:
    j = 6
    while j>=i:
        print(j, end = ' ')
        j-=1
    print()
    i-=1
    
# o/p:
# 1 2 3 4 5 
# 2 3 4 5
# 3 4 5
# 4 5
# 5
# 6
# 6 5
# 6 5 4
# 6 5 4 3
# 6 5 4 3 2
# 6 5 4 3 2 1