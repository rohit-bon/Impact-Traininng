# WAP to find sum of left leaf nodes and sum of right leaf nodes.

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
def depth(root):
    if root is None:
        return 0
    ldepth=depth(root.left)
    rdepth=depth(root.right)
    print("Depth left :",ldepth)
    print("Depth right :",rdepth)
    if(ldepth>rdepth):
        return ldepth+1
    else:
        return rdepth+1
    
def leftLeavesSumRec(root,isleft,summ):
    if root is None:
        return
    # Check whether this is a leaf node and is left
    if root.left is None and root.right is None and isleft==True:
        summ[0] += root.data
        
    # Pass 1 for left and 0 for right
    leftLeavesSumRec(root.left,1,summ)
    leftLeavesSumRec(root.right,0,summ)
    
# A wrapper over above recursive function
def leftLeavesSum(root):
    summ=[0]   # Initialize result
    # Use the above recursive function to evaluate sum
    leftLeavesSumRec(root,0,summ)
    
    return summ[0]
            
b=Node(27)
b.insert(14)
b.insert(35)
b.insert(10)
b.insert(19)
b.insert(31)
b.insert(42)
b.insert(127)
b.insert(156)
print("Sum of left leaves nodes is :",leftLeavesSum(b))