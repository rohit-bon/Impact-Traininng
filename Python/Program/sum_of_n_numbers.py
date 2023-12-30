li=list(input("Enter n values seperated with ,: ").split(","))
sum = 0
for i in li:
    sum = sum + int(i)
print(f"Sum: {sum}")