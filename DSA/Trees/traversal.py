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

def print_tree_pre_order(root):
    if root:
        print(root.data, end = ' ')
        print_tree_pre_order(root.left)
        print_tree_pre_order(root.right)

def print_tree_post_order(root):
    if root:
        print_tree_post_order(root.left)
        print_tree_post_order(root.right)
        print(root.data, end=' ')

n = Node(27)
n.insert(14)
n.insert(35)
n.insert(10)
n.insert(19)
n.insert(31)
n.insert(42)
print_tree_in_order(n)
print()
print_tree_pre_order(n)
print()
print_tree_post_order(n)