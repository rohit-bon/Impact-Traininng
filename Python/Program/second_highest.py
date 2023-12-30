li=list(input("Enter n values seperated with ,: ").split(","))
large=0
slarge=0
for i in li:
    if large < int(i):
        slarge=large
        large = int(i)
    elif int(i) > slarge and int(i) < large:
        slarge = i
print(f"2 Largest element: {slarge}")