def sum_of_numbers(start,end):
    if start == end:
        return end
    else:
        s = start + sum_of_numbers(start+1,end)
    return s
s=sum_of_numbers(1,5)
print(s)


# o/p:
# 15