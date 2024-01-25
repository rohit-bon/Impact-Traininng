i = 1
while i <= 5:
    j = 1
    while j <= i:
        if j%2 == 0:
            print("*",end = ' ')
        else:
            print(j, end=' ')
        j+=1
    print()
    i+=1
    
# o/p:
# 1 
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5