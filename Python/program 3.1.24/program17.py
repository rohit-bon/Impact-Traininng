string1= input()
vowel=0
consonent=0
for i in string1:
    if i in "aeiouAEIOU":
        vowel+=1
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonent +=1
print(f"Vowel count = {vowel}")
print(f"Consonent count = {consonent}")
        