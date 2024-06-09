hash_set = set()
print(type(hash_set))
hash_set.add(10)
hash_set.add(20)
hash_set.add(30)
hash_set.add(40)
print(hash_set)
hash_set.add(10)
print(hash_set)
search_element = 7
if search_element in hash_set:
    print("Element found:")
else:
    print("Not found:")