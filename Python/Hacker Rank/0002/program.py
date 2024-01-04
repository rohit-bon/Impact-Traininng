n = int(input())
a_list = list(map(int, input().split()))[:n]
n = int(input())
b_list = list(map(int, input().split()))[:n]
a_set = set(a_list)
b_set = set(b_list)
res = list(a_set^b_set)
res.sort()
for i in res:
    print(i)
    
# i/P:  
# 4
# 2 4 5 9
# 4 
# 2 4 11 12
# o/p:
# 5
# 9
# 11
# 12