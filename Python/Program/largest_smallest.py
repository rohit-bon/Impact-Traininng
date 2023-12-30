li=list(map(int, input("Enter n values seperated with ,: ").split(",")))
li.sort()
print(f"Smallest element: {li[0]}")
print(f"Largest element: {li[-1]}")


# if __name__ == '__main__':
#     n = int(input())
    
#     num = list(map(int, input().split(",")))
#     for i in num:
#         print(i**2)