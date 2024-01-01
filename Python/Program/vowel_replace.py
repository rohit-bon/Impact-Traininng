string1 = input()
vowel = ['a','e','i','o','u']
res=''
for i in string1:
    if i in vowel:
        ind = vowel.index(i)
        if ind < len(vowel)-2:
            res += vowel[ind+1]
        else:
            res += vowel[0]
    else:
        res += i

print(res)