# Write a program to read a string from the user check whether it is a compressed string or not
# I.p:
# AABBCDEF --> 8
# A2B2C1D1E1F1 --> 12 --> NO
# AAAABBBBCCDD --> 12
# A4B4C2D2 --> 8 --> YES
my_string = input()
my_str_list = [i for i in my_string]
my_str_list.sort()
result = ''
my_str_set = set(my_str_list)
my_list = list(my_str_set)
my_list.sort()
for i in my_list:
    cou = my_str_list.count(i)
    result = result + i + str(cou)
print(result)
if len(my_string) > len(result):
    print("YES")
else:
    print("NO")