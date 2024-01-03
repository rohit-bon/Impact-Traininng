my_string=input()
my_dict = {i:my_string.count(i) for i in my_string if i in 'aeiou'}
print(my_dict)


# o/p:
#     {'a': 1, 'u': 1}