num = int(input())
li=list(map(int,str(num)))
li.sort()
if li[0] == 0:
    temp = li[0]
    li[0] = li[1]
    li[1] = temp

r=list(map(str,li))
print(''.join(r))