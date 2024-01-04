# aabccde ------? a2b1c2d1e1
string = input()
r = set(string)
li = list(r)
li.sort()
res=''
for i in li:
    res+=i+str(string.count(i))
print(res)


# o/p:
# aabccde
# a2b1c2d1e1