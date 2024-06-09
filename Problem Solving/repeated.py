n = int(input())
arr = list(map(int, input().split())) [:n]
result = []
for i in arr:
    if arr.count(i) == 1:
        result.append(i)
if result == []:
    print(0)
else:
    print(result[-1])