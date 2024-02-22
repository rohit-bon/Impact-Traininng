# n1 = int(input())
# n2 = int(input())
# c=0
# for i in range(n1,n2+1):
#     if len(set(str(i))) == len(str(i)):
#         c += 1
# print(c)

# def common_check(num):
#     l = []
#     while(num):
#         l.append(num%10)
#         num = num//10
#     if len(l) == len(set(l)):
#         return True
#     else:
#         return False

def common_check(num):
    l = []
    while(num):
        r = num%10
        if r in l:
            return False
        l.append(r)
        num = num//10
    return True
        

n1 = int(input())
n2 = int(input())
c = 0
for i in range(n1,n2+1):
    d = common_check(i)
    if d:
        c+=1
print(c)