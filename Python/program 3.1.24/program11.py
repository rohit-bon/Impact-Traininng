my_dict={
    "rohit":21,
    "lata":43,
    "sunil":52,
    "gundu":18,
}
list_keys=sorted(my_dict.keys())
dict_keys={}
for i in list_keys:
    dict_keys[i] = my_dict[i]
print(dict_keys)


# o/p:
# {'gundu': 18, 'lata': 43, 'rohit': 21, 'sunil': 52}