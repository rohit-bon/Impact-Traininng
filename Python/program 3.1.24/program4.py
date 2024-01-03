# Write a program to print squares of even numbers from 1 to 20(key is a number and value is square of number)
my_dict={i:i*i for i in range(1,21) if i%2 ==0}
print(my_dict)


# o/p:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}