def new_display(d):
    def smart_display():
        print("*****************")
        d()
        print("*****************")
    return smart_display


@new_display
def display():
    print("Rohit Bongade")
display()

# o/p:
# *****************
# Rohit Bongade
# *****************



def smart_div(d):
    def division(a,b):
        if(b==0):
            return 0
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


# o/p:
# 5.0
# 0