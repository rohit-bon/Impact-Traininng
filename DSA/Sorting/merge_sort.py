def merge(left,right):
    my_list = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            my_list.append(left[i])
            i+=1
        else:
            my_list.append(right[j])
            j+=1
    my_list = my_list + left[i:] + right[j:]
    return my_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        mid = len(my_list)//2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])
    return merge(left,right)

my_list = list(map(int, input().split()))
my_list = merge_sort(my_list)
print(*my_list)