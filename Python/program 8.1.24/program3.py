def value(n):
    assert n<=15 and n>=3, "Value Not in range"
    print(n,"is the Value")
val = int(input())
try:
    value(val)
except(AssertionError):
    print("Value Not in range")
    
# o/p:    
# 2
# Value Not in range

# 5
# 5 is the Value