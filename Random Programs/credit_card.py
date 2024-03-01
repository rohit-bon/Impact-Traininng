# credit_num = int(input())
# even = 0
# odd = 0
# dnum = credit_num
# for i in range(16):
#     if i%2 == 0:
#         n = dnum % 10
#         even += n
#     else:
#         n = dnum % 10
#         odd += n
#     dnum = dnum//10
# print(odd*2,even)
# if ((odd * 2) + even) % 10 == 0:
#     print("Valid Credit card number.",credit_num)
# else:
#     print("InValid Credit card number.",credit_num)

credit_card_number = int(input())
position = 16
even,odd = 0,0
while position > 0:
    if position%2 == 0:
        even += credit_card_number%10
    else:
        odd += credit_card_number%10
    credit_card_number = credit_card_number//10
    position -= 1
print(odd*2,even)
if ((odd * 2) + even) % 10 == 0:
    print("Valid")
else:
    print("Invalid")