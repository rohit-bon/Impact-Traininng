string = input()
r = set(string)
li = list(r)
li.sort()
for i in li:
    if string.count(i) > 1:
        # print(i,"-",string.count(i),end=" ")
        print(f"{i}-{string.count(i)}",end=" ")


# o/p:
# aabbbcd
# a-2 b-3