def bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return my_list

my_list = list(map(int,input().split()))
my_list = bubble_sort(my_list)
print(*my_list)