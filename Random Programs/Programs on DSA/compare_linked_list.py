class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self):
        self.head = None
    
    def add_node(self,data):
        new_node = Node(data)
        temp = self.head
        
        if self.head == None:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def display(self):
        temp = self.head
        
        if self.head == None:
            print("List is Empty.")
        else:
            while temp:
                print(temp.data,end=" ---> ")
                temp = temp.next
            print()
    
    def compare_linked_list(self,list1,list2):
        temp1 = list1.head
        temp2 = list2.head
        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1 is None and temp2 is None:
            return True
        else:
            return False
        

list1 = Single_linked_list()
list1.add_node(10)
list1.add_node(20)
list1.add_node(30)
list1.add_node(40)
list1.display()

list2 = Single_linked_list()
list2.add_node(10)
list2.add_node(20)
list2.add_node(30)
list2.add_node(40)
list2.display()

compare = list1.compare_linked_list(list1,list2)
if compare:
    print("Equal")
else:
    print("Not Equal")
    
    
