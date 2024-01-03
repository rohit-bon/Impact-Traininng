n = int(input())
num_list = list(map(int, input().split()))[:n]
my_dict={i:num_list.count(i) for i in num_list}
li=[-1]
for i,j in my_dict.items():
    if i == j:
        li.append(i)
li.sort()
print(li[-1])
