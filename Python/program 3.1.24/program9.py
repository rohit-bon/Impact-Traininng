my_strinng=input()
my_char=input()
my_dict={i:my_strinng.count(i) for i in my_strinng}
max_value = max(my_dict.values())
li = []
for i,j in my_dict.items():
    if j == max_value:
        li.append(i)
li.sort()
res=''
for i in my_strinng:
    if i == li[0]:
        res += my_char
    else:
        res += i
print(res)


# i/p:
# liril
# t
# o/p:
# ltrtl