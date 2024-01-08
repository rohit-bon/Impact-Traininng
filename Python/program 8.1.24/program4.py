balance = 4000

def withdrraw(amt):
    global balance
    if balance - amt <= 1500:
        raise ValueError
    else:
        print(balance - amt)
try:
    amt = int(input())
    withdrraw(amt)
except(ValueError):
    print("Maintain minimum  balance of 1500.")
    
# o/p:
# 3000
# Maintain minimum  balance of 1500.

# 1000
# 3000