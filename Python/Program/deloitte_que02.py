string1=input()
string2=''
for i in range(len(string1)):
    if string1[i].isnumeric():
        string2+=str(i)
print(string2)