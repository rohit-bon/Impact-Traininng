def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j>=0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j = j-1
        my_list[j+1] = key
        print(my_list)
        
    return my_list

my_list = list(map(int, input().split()))
my_list = insertion_sort(my_list)
print(*my_list)