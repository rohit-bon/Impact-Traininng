string1=input()
n = len(string1)
fibo = [1,1]
f1 = 1
f2 = 1
s = 0
for i in range(n-2):
    s = f1 + f2
    f1 = f2
    f2 = s
    fibo.append(s)
res = [sum(fibo)]
string_list = list(map(str, string1))

for i in range(n):
    res.append(string_list[i])
    res.append(fibo[i])
result=''
for i in res:
    result += str(i)
print(result)




# i/p: abcde
# o/p: 12a1b1c2d3e5