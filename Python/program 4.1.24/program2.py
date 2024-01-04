string = input().split()
n = int(input())
my_dict = {i:string.count(i) for i in string}
remove_list=[]
for i,j in my_dict.items():
    if j >= n:
        remove_list.append(i)
print(" ".join(remove_list))


# o/p:
# cat batman latt matter cat matter cat cat latt latt  
# 3
# cat latt