n=int(input())
li=[]
for i in range (n):
    op=input().split()
    if op[0] == 'insert':
        li.insert(int(op[1]), int(op[2]))
    if op[0] == 'print':
        print(li)
    if op[0] == 'remove':
        li.remove(int(op[1]))
    if op[0] == 'append':
        li.append(int(op[1]))
    if op[0] == 'sort':
        li.sort()
    if op[0] == 'pop':
        li.pop()
    if op[0] == 'reverse':
        li = li[::-1]
        
        
# o/p:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# [6, 5, 10]
# remove 6
# append 9
# append 1
# sort
# print
# [1, 5, 9, 10]
# pop
# reverse
# print
# [9, 5, 1]