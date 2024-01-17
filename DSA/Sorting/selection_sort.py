def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index]>my_list[j]:
                min_index = j
        my_list[min_index],my_list[i] = my_list[i],my_list[min_index]
        # print(my_list)
    return my_list

my_list = list(map(int,input().split()))
my_list = selection_sort(my_list)
print(*my_list)