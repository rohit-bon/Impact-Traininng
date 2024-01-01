string1=input()
count = 0
for i in string1:
    if i.isalpha() or i.isnumeric():
        continue
    else:
        count += 1
print(count)