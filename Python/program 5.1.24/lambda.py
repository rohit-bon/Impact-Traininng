def add(a,b):
    c=a+b
    return c
c=add(10,5)
print(c)

# Lambda 
s = lambda a,b:a+b 
r = s(10,15)
print(r)

#eve numbers
s= lambda x:x%2==0
l = [1,2,3,4,5,6]
r = [i for i in l if s(i)]
print(r)

# odd numbers(30,50)
s= lambda x:x%2!=0
l = []
for i in range(30,50):
    l.append(i)
r = [i for i in l if s(i)]
print(r)