def binary_search(my_list, key):
    my_list.sort()
    low = 0
    high = len(my_list) - 1
    while low<=high:
        mid = (low+high)//2
        if my_list[mid] == key:
            return True
        else:
            if key > my_list[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return False
            
my_list = list(map(int, input().split()))
key = int(input())
found = binary_search(my_list, key)
if found:
    print("Element",key,"is found in list.")
else:
    print("Element not found.")