class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.lch = None
        self.rch = None
    
    # def insert(self,data):
    #     if self.data is None:
    #         self.data = BinaryTree(data)
    #         return
        
    #     if self.lch is None:
    #         self.lch = BinaryTree(data)
        
    #     elif self.rch is None:
    #         self.rch = BinaryTree(data)
        
    #     else:
    #         if self.lch:
    #             self.lch.insert(data)
            
