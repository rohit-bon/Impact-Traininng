num = int(input())
steps = 0
while num > 0:
    divisor = 1
    for i in range(1,num):
        if num % i == 0:
            divisor = i
    num -= divisor
    steps += 1
print(steps)