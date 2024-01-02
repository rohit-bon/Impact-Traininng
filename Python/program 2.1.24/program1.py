l=[1,4,"Rohit","sunil",5,3,"lata",2,"rajshree"]
num_list=[]
string_list=[]
for i in l:
    if type(i) == int:
        num_list.append(i)
    else:
        string_list.append(i)

print(num_list)
print(string_list)
num_list.sort()
string_list.sort()
print(num_list + string_list)