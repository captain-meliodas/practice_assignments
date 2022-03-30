class BST():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def search(self,data):
        found = 'Not Found'

        if self.data == data:
            found = 'Found'
            return found
        
        if data < self.data:
            if self.lchild:
                found = self.lchild.search(data)
        
        else:
            if self.rchild:
                found = self.rchild.search(data)

        return found
    
    def delete(self,data,root_data):
        if self.data is None:
            return "Tree is Empty"
        
        if data < self.data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,self.lchild.data)
            else:
                return "Not Found"
            
        elif data > self.data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,self.rchild.data)
            else:
                return "Not Found"
        else:
            # three case 0 child || 1 child || 2 child
            if self.rchild is None:
                temp = self.lchild
                if root_data == temp.data:
                    self.data = temp.data
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            if self.lchild is None:
                temp = self.rchild
                if root_data == temp.data:
                    self.data = temp.data
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            node = self.rchild
            while node.lchild != None:
                node = node.lchild
            
            self.data = node.data
            self.rchild = self.rchild.delete(node.data,self.rchild.data)

    
root = BST(20)
root.lchild = BST(10)
root.rchild = BST(25)
root.lchild.lchild = BST(5)
root.lchild.rchild = BST(12)
root.rchild.rchild = BST(27)
print(root.search(13))
print(root.delete(20,20))
print(root.data)
        