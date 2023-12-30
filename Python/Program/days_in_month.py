days_31=[1,3,5,7,8,10,12]
days_30=[4,6,9,11]
month=int(input("Enter a month"))
if month==2:
    year = int(input("Enter a year"))
    if year%4==0 and (year%100!=0 or year%400==0):
        print("29 days")
    else:
        print("28 days")
elif month in days_31:
    print("31 days")
elif month in days_30:
    print("30 days")
else:
    print("Invalid")
