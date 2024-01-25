class Node:
    def __init__(self,data):
        self.data = data
        self.left =  None 
        self.right = None 
    
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)

def print_tree_in_order(root):
    if root:
        print_tree_in_order(root.left)
        
        print(root.data, end = ' ')
        
        print_tree_in_order(root.right)

def search_node(root, key):
    if root == None:
        return False
    elif root.data == key:
        return True
    s1 = search_node(root.left, key)
    if s1:
        return True
    s2 = search_node(root.right, key)
    if s2:
        return True

n = Node(27)
n.insert(14)
n.insert(35)
n.insert(10)
n.insert(19)
n.insert(31)
n.insert(42)
print_tree_in_order(n)
print()
key = int(input("Enter Element to search: "))
result = search_node(n, key)
if result:
    print("Element Found")
else:
    print("Element Not Found")