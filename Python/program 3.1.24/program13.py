my_dict={
    "rohit":[39,24,56],
    "lata":[43,53,62],
    "sunil":[52,35,12],
    "gundu":[18,45,67],
}
for i,j in my_dict.items():
    average = sum(j)/len(j)
    print(f"{i} : Average is %.2f"%average)
    
    
    
# o/p:
# rohit : Average is 39.67
# lata : Average is 52.67
# sunil : Average is 33.00
# gundu : Average is 43.33