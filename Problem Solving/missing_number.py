# n = int(input())
# belt_no_list = list(map(int, input().split()))[:n]
# result = []
# for i in range(belt_no_list[0],belt_no_list[-1]+1):
#     if i not in belt_no_list:
#         result.append(i)
# if result == []:
#     result.append(belt_no_list[-1]+1)
# print(*result)


def miss_element(arr, n):
    total = (n+1) * (n+2) // 2
    for i in arr:
        total -= i
    return total

n = int(input())
arr = list(map(int, input().split()))[:n]
x = miss_element(arr, n)
print(x)