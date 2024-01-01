num=int(input())
num2 = num
s=0
while(num!=0):
    r=num%10
    s=(s*10)+r
    num=num//10
if (num2 == s):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")