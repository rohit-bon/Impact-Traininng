my_string = input()
my_dict = {i:my_string.count(i) for i in my_string if i in "aeiou"}
ma=0
max_vowel=''
for i,j in my_dict.items():
    if j >= ma:
        ma = j
        max_vowel = i

print(max_vowel)



# i/p: abeiabfiabgiabdia
# o/p: a


# Logic2:
s=input()
d={i:s.count(i) for i in s if i in "aeiou"}
m=max(d.values())
for i,j in d.items():
    if j == m:
        print(i)


# o/p:     
# maharashtra
# a