n=int(input())
li=list(map(int, input().split()))[:n]
res=[]
for i in li:
    if i not in res:
        res.append(i)
print(*res)