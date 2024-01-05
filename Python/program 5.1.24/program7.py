import math
s=lambda x:math.factorial(x)
print(*[s(i) for i in range(5,11)])


# o/p:
# 120 720 5040 40320 362880 3628800