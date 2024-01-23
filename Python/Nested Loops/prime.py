my_list = []
i=1 
while i<=100:
    c=0
    q=1
    while q<=i:
        if i%q == 0:
            c += 1
        q += 1
    if c == 2:
        my_list.append(i)
    i += 1

print(*my_list)