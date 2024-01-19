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
            
    def insert_at_position(self,data,position):
        node = Node(data)
        temp = self.head 
        if position == 1:
            self.insert_at_start(data)
        else:
            while(position>2):
                temp = temp.next
                position -= 1
            node.next,temp.next=temp.next,node
    
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
    
    def del_at_start(self):
        temp = self.head
        self.head = temp.next 
        self.tail.next = self.head
        
    def del_at_position(self, position):
        temp = self.head
        temp2 = None 
        if position == 1:
            self.del_at_start()
        else:
            while (position > 1):
                temp2 = temp
                temp = temp.next
                position -= 1
                if temp == self.head:
                    if position == 1:
                        print("Enter Valid Position")
                        return 0
                    self.del_at_end()
                    return 0
            temp2.next, temp.next = temp.next, None
        
    def del_at_end(self):
        current = self.head
        temp = self.head.next
        while temp.next != self.head:
            temp = temp.next
            current = current.next
        current.next = self.head
        self.tail=current
            
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
list_obj.insert_at_position(60,3)
list_obj.display()
list_obj.del_at_start()
list_obj.display()
list_obj.del_at_end()
list_obj.display()
# list_obj.insert_at_start(50)
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
# list_obj.display()
# list_obj.reverse()
# list_obj.display()