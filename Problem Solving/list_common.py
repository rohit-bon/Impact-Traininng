list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
for i in list_1:
    if i in list_2:
        print(True)
        break
else:
    print(False)