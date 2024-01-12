li = []
li2 = []
def num(n):
    number = list()
    if n == 0:
        return 0
    else:
        li.append(n)
        num(n-1)
        li2.append(n)
n = int(input())
num(n)
print(li)
print(li2)


# o/p:
# 5
# [5, 4, 3, 2, 1]
# [1, 2, 3, 4, 5]