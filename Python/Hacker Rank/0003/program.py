n = int(input())
a_list = list(map(int, input().split()))[:n]
n = int(input())
b_list = list(map(int, input().split()))[:n]
a_set = set(a_list)
b_set = set(b_list)
li = list(a_set.union(b_set))
print(len(li))

# i/p:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# o/p:
# 13