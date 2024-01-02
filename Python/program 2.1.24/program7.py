num = list(map(int, input().split()))
n = int(input())
for i in num:
    if i == n:
        num.remove(i)
print(num)

# 1 2 6 32 7 3 6 2 6 3 2
# 2
# [1, 6, 32, 7, 3, 6, 6, 3]