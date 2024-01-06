li=[[int(input()) for i in range(3)]for j in range(3)]
s=[]
for i in li:
    r=0
    for j in i:
        r+=j
    s.append(r)
print(s)

s=[0,0,0]
for i in li:
    s[0]+=i[0]
    s[1]+=i[1]
    s[2]+=i[2] 
print(s)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# [6, 15, 24]
# [12, 15, 18]