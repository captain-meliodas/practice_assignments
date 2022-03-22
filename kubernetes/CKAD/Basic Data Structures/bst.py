# Insertion
# Deletion
# searching
# printing in preorder postorder and inorder

class BST():
    def __init__(self,data):
        self.key = data
        self.lchild = None
        self.rchild = None
    
    def printTree(self):
        if self.key:
            print(self.key, end=" ")
        if self.lchild:
            self.lchild.printTree()
        if self.rchild:
            self.rchild.printTree()
    
    def searching(self,search_value):
        if self.key is None:
            # tree is empty
            print("Tree is empty")
            return

        if self.key == search_value:
            print("Number Found")
            return
        
        if search_value < self.key:
            if self.lchild:
                self.lchild.searching(search_value)
            else:
                print("Number Not Found")
                return
        if search_value > self.key:
            if self.rchild:
                self.rchild.searching(search_value)
            else:
                print("Number Not Found")
                return
            
    
    def Insertion(self,data):
        #base case
        if self.key is None:
            self.key = data
            return
        #if data is equal to key we can put it to left or right
        #currently I am making it to left
        if data <= self.key:
            if self.lchild:
                self.lchild.Insertion(data)
            else:
                self.lchild = BST(data)
                return
        
        if data > self.key:
            if self.rchild:
                self.rchild.Insertion(data)
            else:
                self.rchild = BST(data)
                return
    
    def delete(self,data,curr_key):
        if self.key is None:
            #Tree is Empty
            return
        
        if self.key == data:
            # to be going to delete
            # 0 child case can be handle using 1 child as
            # self.lchild will be None in case of 0 child and 
            # return temp will return a None value
            #---------------------
            # 1 child case
            if self.lchild is None:
                temp = self.rchild
                if temp and curr_key == data:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            if self.rchild is None:
                temp = self.rchild
                if temp and curr_key == data:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            #--------------------
            # 2 child case
            # In this case we can replace Node to be deleted
            # with from left tree right most node or righ tree left most
            node = self.rchild
            while node.lchild:
                node = node.lchild

            self.key = node.key
            self.rchild = self.rchild.delete(node.key,self.rchild.key) 
            

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,self.lchild.key)
            else:
                # number is not available
                return
        if data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,self.rchild.key)
            else:
                #number is not available
                return

        #returning the root of the tree
        return self
    
def isSameStructure(a,b):
    #when both are empty
    if a is None and b is None:
        return 1
    #when both are non-empty
    if (a != None and b != None):
        return ( isSameStructure(a.lchild,b.lchild) and isSameStructure(a.rchild, b.rchild) )
    #when one is empty one not
    return 0

def isIdentical(a,b):
    #when both are empty
    if a is None and b is None:
        return 1
    #when both are non-empty
    if (a != None and b != None):
        return ( a.key == b.key and isSameStructure(a.lchild,b.lchild) and isSameStructure(a.rchild, b.rchild) )
    #when one is empty one not
    return 0


root = BST(10)
root.Insertion(20)
root.Insertion(5)
root.Insertion(21)
# root.searching(21)
root.printTree()
print()
# print(root.delete(5,root.key))
# root.printTree()
# print(root.key,root.lchild,root.rchild.key)
root2 = BST(11)
root2.Insertion(21)
root2.Insertion(6)
root2.Insertion(22)
root2.printTree()
print()
print(isSameStructure(root,root2))
print(isIdentical(root,root2))
