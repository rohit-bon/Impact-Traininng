#i/p: a1b2c3d4e
#o/p: e1d2c3b4a
string1=input()
reverseStr=''
for i in string1:
    if i.isalpha():
        reverseStr += i
reverseStr = reverseStr[::-1]
print(reverseStr)
res = ''
j=0
for i in string1:
    if i.isalpha():
        res += reverseStr[j]
        j+=1
    else:
        res += i
print(res)