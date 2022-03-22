class BST():
    def __init__(self,data):
        self.key = data
        self.lch = None
        self.rch = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
        
        if data <= self.key:
            if self.lch:
                self.lch.insert(data)
            else:
                self.lch = BST(data)

        if data > self.key:
            if self.rch:
                self.rch.insert(data)
            else:
                self.rch = BST(data)

def countNodes(root,low,high):
    global count
    temp = list(range(low,high+1))
    if root is None:
        return 0
    
    if root:
        if root.key in temp:
            count+=1
            print(root.key,end=" ")
    
    if root.lch:
        countNodes(root.lch,low,high)
    
    if root.rch:
        countNodes(root.rch,low,high)
count = 0
root = BST(15)
root.insert(10)
root.insert(25)
root.insert(8)
root.insert(12)
root.insert(20)
root.insert(30)
root.insert(0)
root.insert(-1)
root.insert(21)
root.insert(22)
countNodes(root,-1,10)
print()
print(count)