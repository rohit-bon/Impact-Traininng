my_dict={
    "rohit":21,
    "lata":43,
    "sunil":52,
    "gundu":18,
}
list_keys=sorted(my_dict.values())
dict_keys={}
for i in list_keys:
    for j,k in my_dict.items():
        if i == k:
            dict_keys.update({j:k})
print(dict_keys)

# {'gundu': 18, 'rohit': 21, 'lata': 43, 'sunil': 52}