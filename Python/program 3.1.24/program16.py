string1=input()
string2=''
i=len(string1) - 1
while(i!=-1):
    string2 += string1[i]
    i -= 1
if string1 == string2:
    print("Palindrome")
else:
    print("Not palindrome")
    
    
    
    
# o/p:
# nitin
# Palindrome

# rohit
# Not palindrome