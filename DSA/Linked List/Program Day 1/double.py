""" Double Link List"""
"""WAP to to perform add(first,end,at) , del(first,end,at) , Display , Revers"""
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_first(self, i):
        n = Node(i)
        temp = self.head
        if (self.head is None):
            self.head = n
            self.tail = n
        elif(self.tail is None):
            self.tail = n
        else:
            self.head=n
            n.next=temp
            temp.prev=n

    def del_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def add_end(self, i):
        n = Node(i)
        temp = self.head
        temp2=None
        if (self.head is None):
            self.head = n
        else:
            while (temp.next):
                temp2=temp
                temp = temp.next
            temp.next = n
            n.prev=temp2

    def del_end(self):
        temp = self.head
        temp2 = None
        if (self.head is None):
            print("Empty")
        else:
            while (temp.next):
                temp2 = temp
                temp = temp.next
            temp2.next = None

    def add_at(self, i, p):
        n = Node(i)
        temp = self.head
        if (p == 1):
            self.add_first(n)
        else:
            while (p > 2):
                temp = temp.next
                p = p - 1
            n.next, temp.next ,n.prev= temp.next, n,temp

    def del_at(self, p):
        temp = self.head
        temp2 = None
        if (p == 1):
            self.del_first()
        else:
            while (p > 1):
                temp2 = temp
                temp = temp.next
                p = p - 1
                if (temp.next == None):
                    print("Enter Valid Position")
                    break
           # ty=type(temp.next)
            temp2.next, temp.next = temp.next, None



    def dis_revrse(self):
        temp = self.tail
        li = []
        if (self.tail is None):
            print("Empty")
        else:
            while (temp.prev):
                print(temp.data, end="-->")
                temp = temp.prev
            print("\n")
    def Display(self):
        li = []
        temp = self.head
        if (self.head is None):
            print("Empty")
        else:
            while (temp):
                li.append(temp.data)
                temp = temp.next
            for i in li:
                print(i, end="-->")
            print("\n")


n1=Node(10)
#n1.prev=None
d1=Dlist()
d1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
n5=Node(50)
n4.next=n5
n5.prev=n4
d1.tail=n5
d1.add_first(60)
d1.add_end(70)
d1.add_at(80,3)
#d1.del_first()
#d1.del_end()
d1.del_at(22)
d1.Display()
#d1.dis_revrse()