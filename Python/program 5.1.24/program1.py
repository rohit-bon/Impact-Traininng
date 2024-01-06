n = int(input())
count = 0
for i in range(n):
    string = input()
    if len(string) % 2 != 0:
        div = len(string) // 2
        str1 = list(string[0:div])
        str2 = list(string[div+1:])
        str1_dict = {i:str1.count(i) for i in str1}
        str2_dict = {i:str2.count(i) for i in str2}
        flag = 0
        for i,j in str1_dict.items():
            if i not in str1 or i not in str2:
                flag = 1
            else:
                if (str1_dict[i] != str2_dict[i]):
                    falg = 1
        if(flag == 0):
            count += 1        
print(count)


# o/p:
# 5
# aabaaba
# bbaabb
# abbab
# aaabbb
# abbbbabbb
# 3