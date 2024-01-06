import random

def otp_generator():
    i=1
    while(i<=4):
        d=random.randint(1000,10000)
        yield d
        i+=1

otp_g1=otp_generator()
for i in otp_g1:
    print(i)
    
# o/p:
# 4600
# 6994
# 3935
# 3333