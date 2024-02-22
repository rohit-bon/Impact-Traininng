import math
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
prime = []
strange = True
for i in range(2,n):
    if n%i == 0:
        if is_prime(i):
            prime.append(i)
        else:
            strange = False
            break
if is_prime(n):
    prime.append(n)
if strange and prime[-1] > math.sqrt(n):
    print("Strange")
else:
    print("Not Strange")