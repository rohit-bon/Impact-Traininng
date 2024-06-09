list1 = list(map(str, input().split()))
list2 = list(map(int, input().split()))

zipped_lists = zip(list2, list1)

sorted_pairs = sorted(zipped_lists)

sorted_list2 = [pair[0] for pair in sorted_pairs]
sorted_list1 = [pair[1] for pair in sorted_pairs]

print(sorted_list1)
print(sorted_list2)