class BST():
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def preorder(self):
        if self.key:
            print(self.key, end=" ")
        
        if self.lchild:
            self.lchild.preorder()
        
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        
        if self.key:
            print(self.key, end=" ")
        
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        
        if self.rchild:
            self.rchild.postorder()
        
        if self.key:
            print(self.key, end=" ")
    
    def search(self,data):
        if self.key == data:
            print("Node is present in the tree")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")
        
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree")
    
    def insertion(self,data):
        if self.key == None:
            self.key = data
            return

        # if you want to ignore the duplicate value
        # if self.key == data:
        #     return
        
        if  data <= self.key:
            if self.lchild == None:
                self.lchild = BST(data)
            else:
                self.lchild.insertion(data)
        else:
            if self.rchild == None:
                self.rchild = BST(data)
            else:
                self.rchild.insertion(data)
    
    def delete(self,data,root_key):
        if self.key == None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,self.lchild.key)
            else:
                print("Number not found")
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,self.rchild.key)
            else:
                print("Number not found")
        
        else:
            #if node having only left child
            if self.rchild == None:
                temp = self.lchild
                if data == root_key and temp:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                self = None
                return temp
            #if node having only right child
            if self.lchild == None:
                temp = self.rchild
                if data == root_key and temp:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                self = None
                return temp

            #if node is having both child
            node = self.rchild
            while node.lchild:
                node = node.lchild
                
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,self.rchild.key)

        return self

    def minNode(self):
        current = self
        while current.lchild:
            current = current.lchild
        
        return current.key
    
    def maxNode(self):
        current = self
        while current.rchild:
            current = current.rchild
        
        return current.key
    
    def isBst(self):
        if self.key is None:
            return True
        
        if self.lchild and self.lchild.key > self.key:
            return False
        
        if self.rchild and self.rchild.key < self.key:
            return False
        
        if self.lchild:
            if not self.lchild.isBst():
                return False
        
        if self.rchild:
            if not self.rchild.isBst():
                return False
        
        return True

root = BST(10)
# A = []
A = [6,3,1,98,7]
# A = [1,34,21,3,5,1,2,11]

for data in A:
    root.insertion(data)

root.search(40)
root.preorder()
print("Preorder")
root.inorder()
print("Inorder")
# root.delete(10,root.key)
# root.delete(98,root.key)
print("Postorder")
root.postorder()
print()
print(root.maxNode())
print(root.minNode())
print(root.isBst())