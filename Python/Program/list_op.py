l=[1,2,3,4,5]
i=0
while(i<len(l)):
    print(l[i],end=" ")
    i+=1
print()
for p in l:
    print(p,end=" ")
print()
for i in range(len(l)):
    print(i,l[i])
print(max(l))
print(min(l))
print(sum(l))
avg=sum(l)/len(l)
print(avg)