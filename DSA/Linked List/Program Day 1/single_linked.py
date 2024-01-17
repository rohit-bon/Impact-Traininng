"""Link List"""
"""WAP to to perform add(first,end,at) , del(first,end,at) , Display , Reveres on Single linklist"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Slist:
    def __init__(self):
        self.head=None
    def add_first(self,i):
        n=Node(i)
        if(self.head is None):
            self.head = n
        else:
            self.head,n.next=n,self.head
    def del_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def add_end(self,i):
        n=Node(i)
        temp = self.head
        if (self.head is None):
            self.head=n
        else:
            while (temp.next):
                temp = temp.next
            temp.next = n
    def del_end(self):
        temp = self.head
        temp2=None
        if (self.head is None):
            print("Empty")
        else:
            while (temp.next):
                temp2=temp
                temp = temp.next
            temp2.next =None

    def add_at(self,i,p):
        n=Node(i)
        temp = self.head
        if(p==1):
            self.add_first(n)
        else:
            while (p>2):
                temp = temp.next
                p=p-1
            n.next,temp.next=temp.next,n

    def del_at(self,p):
        temp = self.head
        temp2=None
        if (p == 1):
            self.del_first()
        else:
            while (p > 1):
                temp2=temp
                temp = temp.next
                p = p - 1
            temp2.next,temp.next = temp.next,None

    """WAP to reverse link list element without using list """
    
    def dis_revrse(self):
        temp = self.head
        li = []
        if (self.head is None):
            print("Empty")
        else:
            while (temp):
                li.append(temp.data)
                temp = temp.next
            for i in li[::-1]:
                print(i, end="-->")
            print("\n")

    def Display(self):
        temp=self.head
        li=[]
        if(self.head is None):
            print("Empty")
        else:
            while(temp):
                li.append(temp.data)
                temp=temp.next
            for i in li:
                print(i,end="-->")
            print("\n")
#n1=Node(10)
s1=Slist()
#s1.head=n1
s1.add_first(10)
s1.add_end(20)
s1.add_end(30)
s1.add_end(40)
s1.dis_revrse()
s1.add_first(50)
s1.add_end(60)
s1.add_at(70,4)
s1.del_first()
s1.del_end()
s1.del_at(3)
s1.Display()