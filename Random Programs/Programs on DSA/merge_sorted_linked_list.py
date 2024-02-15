#Write a program to merge the 2 sorted linked list

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
            
    def merge_two_list(self,list1,list2):
        l1 = list1.head
        l2 = list2.head
        list3 = []
        if l1 is None and l2 is None:
            print("Both list are Empty")
        else:
            while l1 and l2:
                if l1.data > l2.data:
                    list3.append(l2.data)
                    l2 = l2.next
                else:
                    list3.append(l1.data)
                    l1 = l1.next
            if l1 != None:
                while l1:
                    list3.append(l1.data)
                    l1 = l1.next
            elif l2 != None:
                while l2:
                    list3.append(l2.data)
                    l2 = l2.next
        print("New List")
        for i in list3:
            print(i,end=" ---> ")
                

list1 = Single_linked_list()
list1.add_node(1)
list1.add_node(3)
list1.add_node(5)
list1.add_node(7)
list1.add_node(9)
list1.display()

list2 = Single_linked_list()
list2.add_node(2)
list2.add_node(4)
list2.add_node(6)
list2.add_node(8)
list2.add_node(10)
list2.display()

list1.merge_two_list(list1,list2)

# list1 = Single_linked_list()
# list2 = Single_linked_list()
# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
# for i in l1:
#     list1.add_node(i)
# for i in l2:
#     list2.add_node(i)
# list1.merge_two_list(list1,list2)