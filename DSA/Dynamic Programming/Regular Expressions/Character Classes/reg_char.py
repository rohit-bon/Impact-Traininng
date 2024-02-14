# import re
# l=re.finditer("[abc]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")
# l=re.finditer("[^abc]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")
# l=re.finditer("[a-z]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")
# l=re.finditer("[a-zA-Z]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")

# l=re.finditer("[0-9]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")
# l=re.finditer("[a-zA-Z0-9]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())
# print("------------------------------------------------------------------------------")
# l=re.finditer("[^a-zA-Z0-9]","a7b@K9z")
# for p in l:
#     print(p.start(),"---",p.group())


import re
l=re.finditer("\s","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer("\S","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer("\d","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer("\D","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer("\w","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer("\W","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())
print("------------------------------------------------------------------------------")
l=re.finditer(".","a7b @K9z")
for p in l:
    print(p.start(),"---",p.group())