# >4000 ---> 4%
# >3000 ---> 3%
# >2000 ---> 2%
# >1000 ---> 1%
# <1000 ---> No discount 
# after discount display final balance

name = input("ENTER YOUR NAME: ")
amt = int(input("Enter amount: "))

if amt >= 4000:
    print(f"Discount is 4% : Rs. {(amt/100) * 4 } amount you have to pay is {amt - (amt/100) * 4}")
elif amt >= 3000:
    print(f"Discount is 3% : Rs. {(amt/100) * 3 } amount you have to pay is {amt - (amt/100) * 3}")
elif amt >= 2000:
    print(f"Discount is 2% : Rs. {(amt/100) * 2 } amount you have to pay is {amt - (amt/100) * 2}")
elif amt >= 1000:
    print(f"Discount is 1% : Rs. {(amt/100) * 1 } amount you have to pay is {amt - (amt/100) * 1}")
else:
    print(f"No Discount.")