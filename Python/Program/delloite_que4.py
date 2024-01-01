# sort number in descending order
num = int(input())
li=list(map(int,str(num)))
li.sort(reverse=True)
print(li)
r=list(map(str,li))
print(''.join(r))
# for i in li:
#     print(i,end="")