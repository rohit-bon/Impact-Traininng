from collections import deque

stack = deque()

stack.append("Rohit")
stack.append("4+8r")
stack.append(4.5)
stack.append(2003)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)