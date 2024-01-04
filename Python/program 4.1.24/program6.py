string1 = input()
string2 = input()

set1 = set(string1)
set2 = set(string2)

res_list = list(set1.intersection(set2))
res_list.sort()

res=''
for i in res_list:
    res += i
print(res)


# i/p:
# beads
# leaps
# o/p:
# aes