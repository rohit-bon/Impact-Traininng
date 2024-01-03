n=int(input())
my_dict={}
for i in range(n):
    my_input = input().split()
    my_list=[int(my_input[1]),int(my_input[3]),int(my_input[3])]
    my_dict.update({my_input[0]:my_list})
res=input()
average = sum(my_dict[res])/len(my_dict[res])
# print(my_dict)
print("%.2f"%average)


# i/p:
# 3
# rohit 23 34 45
# sunil 34 45 56
# lata 56 67 67
# sunil
# o/p:
# 48.67