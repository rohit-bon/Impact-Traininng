s=input()
s=s.lower()
r=''
for i in range(97, 123):
    d=chr(i)
    if d not in s:
        r=r+d
print(r)