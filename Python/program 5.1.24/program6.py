def replace_string(my_string, sub, new):
    res = my_string.replace(sub, new)
    return res
string = input()
sub = input()
new = input()
res =  replace_string(string, sub, new)
print(res)


# o/p:
# Hi Rohit
# Hi
# Hello
# Hello Rohit