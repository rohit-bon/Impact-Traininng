# n = int(input())
# my_list = list(map(int,input().split()))[:n]
# result = []
# for i in range(n-1):
#     if my_list[i] < my_list[i+1]:
#         result.append(my_list[i+1])
#     else:
#         result.append(-1)
# result.append(-1)
# print(*result)


n = int(input())
l = list(map(int,input().split()))[:n]
stack = []
result = [0]*n

for i in range(n):
    while stack and l[i] > l[stack[-1]]:
        index = stack.pop()
        result[index] = l[i]
    stack.append(i)

while stack:
    index = stack.pop()
    result[index] = -1
    
print(*result)