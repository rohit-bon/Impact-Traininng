i = 5
while i<=10:
    fact = 1
    j = 1
    while j<=i:
        fact *= j
        j += 1
    print(fact)
    i += 1