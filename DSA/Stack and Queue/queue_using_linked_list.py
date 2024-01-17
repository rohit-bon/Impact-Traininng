# Implementation of Queue using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.rear = 1
        self.size = 5
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def isFull(self):
        if self.rear > self.size:
            return True
        else:
            return False
        
    def push(self,data):
        if self.isFull():
            print("Queue is Full")
        else:
            if self.head == None:
                self.head = Node(data)
                self.rear +=1
            else:
                temp = self.head
                new = Node(data)
                self.head = new
                new.next = temp
                self.rear +=1
    
    def display(self):
        temp = self.head
        if self.isEmpty():
            print("Queue is Empty.")
        else:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    
    def pop(self):
        temp = self.head
        dummy_node = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            while temp.next:
                dummy_node = temp
                temp = temp.next
            if dummy_node is not None:
                dummy_node.next = None
            else:
                self.head = None
            print(temp.data,"is pop")
            
                
Queue_object = Queue()
Queue_object.display()
Queue_object.push(10)
Queue_object.push(20)
Queue_object.push(30)
Queue_object.push(40)
Queue_object.push(40)
Queue_object.push(30)
Queue_object.display()
Queue_object.pop()
Queue_object.display()
Queue_object.pop()
Queue_object.display()
Queue_object.pop()
Queue_object.display()
Queue_object.pop()
Queue_object.display()
