class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        if lh < rh:
            return rh + 1
        else:
            return lh + 1

def printCurrentLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data,end=" ")
    
    if level > 1:
        printCurrentLevel(root.left,level-1)
        printCurrentLevel(root.right,level-1)

def printLevelOrder(root):
    h = height(root)

    for i in range(1,h+1):
        printCurrentLevel(root,i)

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)