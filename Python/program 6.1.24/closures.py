def power(i):
    def pow(n):
        return i**n
    return pow
s=power(5)
r=s(4)
print(r)

# o/p:
# 625

s=power(4)
p=s(3)
print(p)

# o/p:
# 64