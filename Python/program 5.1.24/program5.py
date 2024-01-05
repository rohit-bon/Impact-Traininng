def check_palindrome(my_list):
    flag = True
    for i in my_list:
        i=str(i)
        if i != i[::-1]:
            flag = False
    return flag
n = int(input())
my_List = list(map(int, input().split()))[:n]
res = check_palindrome(my_List)
if res:
    print("Yes")
else:
    print("No")
    

# 3
# 121 131 444
# Yes