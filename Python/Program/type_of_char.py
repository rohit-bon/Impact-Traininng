ch = input("Enter a character")
if(ch >= 'A') and (ch <= 'Z'):
    print("uppercase character")
elif(ch >= 'a') and (ch <= 'z'):
    print("lowercase character")
elif(ch >= '0') and (ch <= '9'):
    print("digit")
else:
    print("special character")