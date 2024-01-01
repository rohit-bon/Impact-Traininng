#i/p:
    # 5
    # 1 2 3 4 5
    # 2

#o/p: 
    # 4 5 1 2 3


n=int(input())
li = list(map(int, input().split(" ")))[:n]
r=int(input())
d=[]
d=li[-r:]+li[:-r]
print(*d)