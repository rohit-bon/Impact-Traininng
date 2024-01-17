class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class single_list:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp = self.head
        
        if self.head is None:
            print("List is Empty:")
        else:
            while(temp):
                print(temp.data,end="--->")
                temp = temp.next
        print()
    
    def reverse_display(self):
        reverse_list = []
        temp = self.head
        if self.head is None:
            print("List is Empty")
        else:
            while(temp):
                reverse_list.append(temp.data)
                temp = temp.next
        reverse_list.reverse()
        for i in reverse_list:
            print(i,end='--->')
            
    def insert_at_start(self,data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp
        
    def insert_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
    
n1 = Node(10)
single_object = single_list()
single_object.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
single_object.display()
single_object.insert_at_start(5)
single_object.display()
single_object.insert_at_end(50)
single_object.display()
single_object.reverse_display()
