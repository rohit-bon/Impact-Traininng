def linear_search(my_list,key):
    for i in range (len(my_list)):
        if my_list[i] == key:
            return i
    return -1
        
my_list = list(map(int, input().split()))
key = int(input())
found = linear_search(my_list, key)
if found == -1:
    print("Element not found.")
else:
    print("Element",key,"fount at",found+1,"Position and Index is",found)