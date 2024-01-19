my_dict = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4"
}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())

for i in my_dict.values():
    pos = val_list.index(i)
    key = key_list[pos]
    print(key,"is the key for value",i)


print(list(my_dict.keys()) [list(my_dict.values()).index("value1")])