# Implementation of stack using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            new = Node(data)
            self.head = new
            new.next = temp
    
    def display(self):
        temp = self.head
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    
    def pop(self):
        temp = self.head
        dummy_node = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            dummy_node = temp.next
            self.head = dummy_node
            print("Deleted Element is:", temp.data)
            
                
stack_object = Stack()
stack_object.display()
stack_object.push(10)
stack_object.push(20)
stack_object.push(30)
stack_object.push(40)
stack_object.display()
stack_object.pop()
stack_object.display()
