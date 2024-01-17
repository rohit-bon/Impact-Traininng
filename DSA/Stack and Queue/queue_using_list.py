queue = []
size = int(input("Enter Size:"))
top = -1
while True:
    print("MENU")
    print("1. Push \n2. Pop \n3. Display \n4. Exit")
    option = int(input("Enter your Selection: "))
    if option == 1:
        if top < size -1:
            top +=1
            element = int(input("Enter Element: "))
            queue.append(element)
        else:
            print("queue is Full")
    elif option == 2:
        if top == -1:
            print("queue is empty")
        else:
            print("Poped element is",queue.pop(0))
            top = top-1
    elif option == 3:
        print(queue)
    elif option == 4:
        break
    else:
        print("Wrong Option")
