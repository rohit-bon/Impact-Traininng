def fact_of_number(number):
    if number == 0:
        return 1
    else:
        num = number * fact_of_number(number - 1)
    return num

fact = fact_of_number(5)
print(fact)


# o/p:
# 120