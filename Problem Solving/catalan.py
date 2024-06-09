def catalan(n):
    if n==0 or n==1:
        return 1
    
    catalan = [0]*(n+1)

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    
    return catalan[n]

for i in range(10):
    print(catalan(i), end=" ")
