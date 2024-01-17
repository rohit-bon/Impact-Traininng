# Implementation of Stack using List

stack = []
size = int(input("Enter the  size of stack: "))
top = -1
while True:
    print("MENU")
    print("1. Push \n2. Pop \n3. Display \n4. Exit")
    option = int(input("Enter your Selection: "))
    if option == 1:
        if top < size -1:
            top +=1
            element = int(input("Enter Element: "))
            stack.append(element)
        else:
            print("Stack is Full")
    elif option == 2:
        if top == -1:
            print("Stack is empty")
        else:
            print("Poped element is",stack.pop())
            top = top-1
    elif option == 3:
        print(stack)
    elif option == 4:
        break
    else:
        print("Wrong Option")
