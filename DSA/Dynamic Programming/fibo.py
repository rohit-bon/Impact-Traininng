def fib(n):
    f=[0,1]
    for p in range(2,n+1):
        f.append(f[p-1]+f[p-2])
    return f[n]
print(fib(9))