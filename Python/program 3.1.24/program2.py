n=int(input())
num_list = list(map(int, input().split()))
leader_ele = []
for i in range(len(num_list)):
    flag = True
    for j in range(i, len(num_list)):
        if num_list[i] < num_list[j]:
            flag = False
    if flag:
        leader_ele.append(num_list[i])
sum = 0
for i in leader_ele:
    sum = sum+i
print(sum)

# i/p:
# 7
# 52 66 64 36 45 24 32
# o/p:
# 207