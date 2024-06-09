list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
if len(list1) == len(list2):
    for i in list1:
        if i not in list2:
            print(False)
            break
    else:
        for i in list2:
            if i not in  list1:
                print(False)
                break
        else:
            print(True)
else:
    print(False)