car1_speed = int(input())
car2_speed = int(input())
difference = int(input())
inital_start1 = 0
inital_start2 = 0 - difference
seconds = 0
if car1_speed >= car2_speed:
    print(-1)
else:
    while inital_start1 >= inital_start2:
        inital_start1 += car1_speed
        inital_start2 += car2_speed
        seconds += 1
    print(seconds)

# a = int(input())
# b = int(input())
# d = int(input())
# n1 = 0
# n2 = d
# c=0
# while n1>n2:
#     if a>b:
#         c=-1
#         break
#     else:
#         n1 += a
#         n2 += b
#         c+=1
# print(c)