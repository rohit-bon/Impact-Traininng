s1=float(input("Enter side 1: "))
s2=float(input("Enter side 2: "))
s3=float(input("Enter side 3: "))

if (s1**2 + s2**2 == s3**2) or (s3**2 + s2**2 == s1**2) or (s1**2 + s3**2 == s2**2):
    print("Yes, Right angle Triangle")
else:
    print("No, Right angle Triangle")