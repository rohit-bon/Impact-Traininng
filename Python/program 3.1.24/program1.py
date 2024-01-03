n=int(input())
count = 0
number_list=[]
for i in range(n):
    string1=input()
    string_list=list(map(str, string1))
    num=''
    for j in range(10):
        num += string_list[j]
    age = int(string_list[-4]+string_list[-3])
    if age>= 60:
        count += 1
        number_list.append(num)
print(count)
print(*number_list)


# i/p:
# 3
# 7972590082M2312
# 9923717793M6103
# 7867564534M3212
# o/p:
# 1
# 9923717793