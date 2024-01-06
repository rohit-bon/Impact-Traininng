def smart_div(d):
    def division(a,b):
        if(b==0):
            return 0
        elif type(b) == str:
            return b
        else:
            return d(a,b)
    return division

@smart_div
def div(a,b):
    return a/b
a=div(10,2)
print(a)
a=div(10,0)
print(a)
a=div(10,'asdf')
print(a)


# o/p:
# 5.0
# 0
# asdf