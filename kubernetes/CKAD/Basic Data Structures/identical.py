# Input
# 5
# 1 3 2 4 -1
# 4 1 2 3 -1
# 3 2 1 4 -1
# 4 3 2 1 -1
# 1 3 4 2 -1

# Output

# NO 1
# NO 0
# NO 1
# YES 0
# (Note that the depth difference will be zero if the trees are equivalent.)

# In this problem you have to write a program to check if two given binary trees are structurally equivalent.
# Two trees are structurally equivalent if they are both null or if the left and right children of one are 
# structurally equivalent to the RESPECTIVE children of the other. 
# In other words, when you draw the trees on paper, they should LOOK alike (ignoring the values at the nodes).
# Construct a binary search tree with the input in the second line and use this as the basis-tree. 
# For each of the remaining N-1 lines, construct a binary search tree and compare against the basis tree for equivalence. 
# If the trees are equivalent, print YES else print NO. Also print the depth difference between the two trees 
# (ie, depth of the bigger tree minus the depth of the smaller tree). Both these for a given tree pair must be on one line separated 
# by a space.
# The answers for the different pairs must be on separate lines.

class BST():
    def __init__(self,data):
        self.key = data
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
        
        if data <= self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
def maxDepth(root):
    if root is None:
        return -1
    else:
        ldepth = maxDepth(root.lchild)
        rdepth = maxDepth(root.rchild)

        if ldepth > rdepth:
            return (ldepth + 1)
        else:
            return (rdepth + 1)

def isSame(root1,root2):
    if root1 is None and root2 is None:
        return 1
    
    if root1 != None and root2 != None:
        return (isSame(root1.lchild, root2.lchild) and isSame(root1.rchild,root2.rchild))

    return 0

# 5
# 1 3 2 4 -1
# 4 1 2 3 -1
# 3 2 1 4 -1
# 4 3 2 1 -1
# 1 3 4 2 -1
cases = int(input())
root1_list = input().split(" ")
root1 = BST(None)
left = maxDepth(root1)
for i in range(len(root1_list)-1):
    root1.insert(int(root1_list[i]))

for i in range(cases-1):
    root2_list = input().split(" ")
    root2 = BST(None)
    for index in range(len(root2_list)-1):
        root2.insert(int(root2_list[index]))
    check = isSame(root1,root2)
    right = maxDepth(root2)
    if check:
        print("YES 0")
    else:
        print("NO",abs(left-right))