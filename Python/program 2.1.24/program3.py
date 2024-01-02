n=int(input())
li=list(map(int,input().split()))[:n]
res=[]
li.sort()
count=len(li) - 1
ind=0
for i in range(len(li)):
    if i % 2 == 0:
        res.append(li[ind])
        ind +=1
    else:
        res.append(li[count])
        count -= 1
print(*res)

# o/p: 
# 7
# 5 2 3 4 6 5 -2
# -2 6 2 5 3 5 4

# logic 2
r=[]
for i in range(len(li)//2):
    r.append(li[i])
    r.append(li[-(i+1)])
if(len(li) % 2 !=0):
    r.append(li[len(li)//2])
print(*r) 