def even(n):
    assert n%2 == 0, "The number should be even"
    print(n,"is even")
even(10)
even(5)


# o/p:
# 10 is even
# Traceback (most recent call last):
#   File "d:\Impact Traininng\Python\program 8.1.24\program2.py", line 5, in <module>
#     even(5)
#   File "d:\Impact Traininng\Python\program 8.1.24\program2.py", line 2, in even
#     assert n%2 == 0, "The number should be even"
# AssertionError: The number should be even

def even(n):
    assert n%2 == 0, "The number should be even"
    print(n,"is even")
try:
    even(10)
    even(5)
except(AssertionError):
    print("Number should be even")
    
# o/p:
# 10 is even
# Number should be even