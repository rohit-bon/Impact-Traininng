# import re
# c=0
# p=re.finditer("ab","abaabab")
# for s in p:
#     c=c+1
#     print(s.start(),"---",s.end(),"---",s.group())
# print("No. of occurences:",c)

# import re
# p=re.match("In","India")
# if p!=None:
#     print("The Pattern available at begining of string:")
# else:
#     print("The Pattern is not available at begining of string:")

# import re
# p=re.fullmatch("India","India-Rohit")
# if p!=None:
#     print("The Pattern Matched")
# else:
#     print("The Pattern not Matched")

# import re
# p=re.search("in","ashwin")
# if p!=None:
#     print("The Pattern is available")
# else:
#     print("The Pattern is not available")

# import re
# l=re.findall("[0-9]","a1b3ghd2")
# print(l)

# import re
# l=re.finditer("[a-z]","a1b3ghd2")
# for p in l:
#     print(p.start(),"---",p.end(),"---",p.group())

# import re
# l=re.sub("[0-9]","$","a1b3ghd2")
# print(l)

# import re
# l=re.subn("[0-9]","$","a1b3ghd2")
# print(l)

# import re
# l=re.search("^learn","learning with python is easy")
# if l!=None:
#     print("The given str starts with learns")
# else:
#     print("The given str not starts with learns")
    
    
import re
l=re.search("easy$","learning with python is easy")
if l!=None:
    print("The given str ends with easy")
else:
    print("The given str not ends with easy")