s=input()
otp = ''
for i in s:
    num = int(i)
    if num%2!=0:
        otp = otp+ str(num**2)
print(otp)