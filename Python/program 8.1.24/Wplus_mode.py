file_location = open("D:\Impact Traininng\Python\program 8.1.24\Files Program\Actor.txt","w+")
file_location.write("Ranbir Kapoor\nSalman\nSharukh\nRanveer\nKartik")
file_location.seek(0)
print(file_location.read())
file_location.close()


# o/p:
#   file_location = open("D:\Impact Traininng\Python\program 8.1.24\Files Program\Actor.txt","w+")
# Ranbir Kapoor
# Salman
# Sharukh
# Ranveer
# Kartik