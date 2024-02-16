n1, n2, n3 = map(int, input().split())
stack1 = list(map(int, input().split()))
stack2 = list(map(int, input().split()))
stack3 = list(map(int, input().split()))
sum1, sum2, sum3 = sum(stack1), sum(stack2), sum(stack3)
while sum1 != sum2 or sum1 != sum3:
    if sum1 > sum2 and sum1 > sum3:
        sum1 -= stack1.pop(0)
    elif sum2 > sum1 and sum2 > sum3:
        sum2 -= stack2.pop(0)
    else:
        sum3 -= stack3.pop(0)
        
print(sum1)