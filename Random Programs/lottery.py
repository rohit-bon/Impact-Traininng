N, K = map(int, input().split())
result = []
l = 0
i=2
while (l<N):
    c=0
    for j in range(1, i+1):
        if(i%j == 0):
            c=c+1
    if(c==2):
        num = i%10
        if i == 2 or i == 5:
            result.append(i)
        if num == K:
            result.append(i)
            l+=1
    i+=1
print(*result)