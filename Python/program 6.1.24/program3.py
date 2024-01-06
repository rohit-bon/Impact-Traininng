def outer(i):
    def inner(n):
        print(i*n)
    return inner
s=outer("*")
s(11)
s=outer("$")
s(11)


# o/p:
# ***********
# $$$$$$$$$$$