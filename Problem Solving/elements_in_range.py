# n = int(input())
# elements_list = list(map(int, input().split()))[:n]
# start_range, end_range = map(int, input().split())
# range_list = [i for i in range(start_range,end_range+1)]
# element_count = 0
# for i in elements_list:
#     if i in range_list:
#         element_count += 1
# print(element_count)

# n, count_ele = int(input()), 0
# elements_list = list(map(int, input().split()))[:n]
# start_range, end_range = map(int, input().split())
# for i in elements_list:
#     if i in range(start_range, end_range+1):
#         count_ele+=1
# print(count_ele)

n = int(input())
elements_list = list(map(int, input().split()))[:n]
start_range, end_range = map(int, input().split())
range_element = [i for i in elements_list if i in range(start_range, end_range+1)]
print(len(range_element))