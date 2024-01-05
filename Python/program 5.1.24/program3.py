def even_odd(n):
    if (n%2 == 0):
        return 0
    else:
        return 1
n = int(input())
r = even_odd(n)
if(r==0):
    print(n,"is even")
else:
    print(n,"is odd")
    
    
# o/p:
# 10 
# 10 is even