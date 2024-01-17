vowels = 'aeiouAEIOU'
consonant = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTWXYZ'
cou = 0
my_string = input()
for i in range(len(my_string)-1):
    if my_string[i] in vowels:
        if my_string[i+1] in consonant:
            cou += 1
print(cou)


# o/p:
# OqPputLE
# 2

# iamneo@
# 1