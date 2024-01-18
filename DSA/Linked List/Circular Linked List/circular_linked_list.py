class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def display(self):
        if self.head is None:
            print("List is Empty.")
        else:
            temp = self.head
            while(True):
                print(temp.data,end="--->")
                temp = temp.next
                if temp == self.head:
                    break
            print(temp.data)
            
    def insert_at_start(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            temp = self.head
            node = Node(data)
            node.next = temp
            self.head = node
            self.tail.next = node
    
    def insert_at_last(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            
    def reverse(self):
        prev = self.tail
        current = self.head
        while(True):
            next = current.next
            current.next = prev
            prev = current
            current = next
            if current == self.head:
                break
        self.head = prev
# n1 = Node(10)
list_obj = circular_linked_list()
# list_obj.head = n1
# list_obj.tail = n1
# list_obj.tail.next = list_obj.head
list_obj.insert_at_start(10)
list_obj.insert_at_last(20)
list_obj.insert_at_last(30)
list_obj.insert_at_last(40)
list_obj.display()
list_obj.insert_at_start(50)
# n2 = Node(20)
# list_obj.tail.next = n2
# list_obj.tail = n2
# list_obj.tail.next = list_obj.head
# n3 = Node(30)
# list_obj.tail.next = n3
# list_obj.tail = n3
# list_obj.tail.next = list_obj.head
# n4 = Node(40)
# list_obj.tail.next = n4
# list_obj.tail = n4
# list_obj.tail.next = list_obj.head
list_obj.display()
list_obj.reverse()
list_obj.display()