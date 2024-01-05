def weight_of_string(string):
    s = 0
    for i in string:
        weight = 10**(ord(i)-ord('A'))
        s += weight
    return s
string = input()
res=weight_of_string(string)
print(res)


# p/p:
# DCCBAA
# 1212