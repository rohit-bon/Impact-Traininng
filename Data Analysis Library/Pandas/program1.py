import pandas as pd

my_dict = {
    "Names" : ["Rohit", "Sunil", "Rani"],
    "Roll" : [101,102,103],
    "Maths" : [67,78,92],
    "English" : [56,67,45],
    "Physics" : [78,89,90]
}

df = pd.DataFrame(my_dict)
print(df)
print()
print(df.columns)
print()
print(df.shape)
print()
print(df[["Names","English"]])
print()
print(df.head(2))
print()
print(df.tail(2))
print()
new_dict = {
    "Names" : "Lata",
    "Roll" : 104,
    "Maths" : 78,
    "English" : 88,
    "Physics" : 99
}
df = df._append(new_dict,ignore_index=True)
print(df)
print()
print(df[:])
print()
print(df[1:3])
print()
print(df[0:4])
print()
new_dict1 = {
    "Names" : "Dhyani",
    "Roll" : 105,
    "Maths" : 72,
    "English" : 78,
    "Physics" : 89
}
new_dict2 = {
    "Names" : "Rohini",
    "Roll" : 106,
    "Maths" : 74,
    "English" : 68,
    "Physics" : 79
}
df = df._append(new_dict1, ignore_index=True)
df = df._append(new_dict2, ignore_index=True)
print(df)
print()
df["Marathi"] = [98,92,78,88,78,76]
print(df)
print()
print(df.loc[3])
print()
print(df.loc[1:3])
print()
print(df.loc[:3])
print()
print(df.loc[2:])
print()
print(df.loc[1:3, "Names":"Maths"])
print()
print(df.iloc[1:3])
print()
print(df.iloc[1:3,1:3])
print()
print(df.iloc[:,2:5])
print()