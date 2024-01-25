i=1
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print("*", end=' ')
        else:
            print(j, end=' ')
        j+=1
    print()
    i+=1
    
# o/p:
# 1 
# * *
# 1 2 3
# * * * *
# 1 2 3 4 5