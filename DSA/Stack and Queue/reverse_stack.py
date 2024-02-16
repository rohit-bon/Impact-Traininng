class Stack:
    def __init__(self):
        self.stack = []
    
    def push_data(self,data):
        self.stack.append(data)
        
    def pop_data(self):
        if self.stack:
            print("Deleted element is:",self.stack.pop())
        else:
            print("Stack is Underflow")
    
    def display_stack(self):
        print(self.stack)
        
    def reverse_stack(self):
        self.stack.reverse()
    
stack_object = Stack()
stack_object.pop_data()
stack_object.push_data(5)
stack_object.push_data(3)
stack_object.push_data(8)
stack_object.push_data(1)
stack_object.push_data(7)
stack_object.pop_data()
stack_object.push_data(2)
print("Stack before Reverse")
stack_object.display_stack()
stack_object.reverse_stack()
print("Stack after Reverse")
stack_object.display_stack()