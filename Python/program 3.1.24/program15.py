my_dict={
    "Rohit" : {
        "python" : 35,
        "flutter" : 100,
        "django" : 67
    },
    "Karan" : {
        "python" : 55,
        "flutter" : 30,
        "django" : 54
    },
    "Kartik" : {
        "python" : 65,
        "flutter" : 50,
        "django" : 76
    }
}
for i in my_dict.keys():
    marks = my_dict[i].values()
    print(i)
    print("-------------------------")
    for j in marks:
        print(j)
    print("\n")
    
    
# o/p:
# Rohit
# -------------------------
# 35
# 100
# 67


# Karan
# -------------------------
# 55
# 30
# 54


# Kartik
# -------------------------
# 65
# 50
# 76
