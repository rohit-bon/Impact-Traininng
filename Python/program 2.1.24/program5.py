num = int(input())
num_list=list(map(int,str(num)))
even_list=[]
odd_list=[]
# res=[even_list(i) if(i%2==0) else odd_list(i) for i in num_list]
for i in num_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.reverse()
odd_list.sort()
res= odd_list + even_list
res = int("".join([str(i) for i in res]))
print(res)

# i/p: 2143658709
# o/p: 1357908642