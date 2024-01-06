def factorial_gen(val1,val2):
    for i in range(val1,val2+1):
        fact=1
        for j in range(1,i+1):
            fact*=j
        yield fact
fact_gen = factorial_gen(5,10)
for i in fact_gen:
    print(i)
    
    
# o/p:
# 120
# 720
# 5040
# 40320
# 362880
# 3628800