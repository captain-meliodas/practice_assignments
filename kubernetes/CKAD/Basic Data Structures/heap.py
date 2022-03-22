#min heap
import sys
class MinHeap():
    def __init__(self,maxsize):
        #max size of the heap
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
    
    # parent
    def parent(self,pos):
        return pos // 2
    
    # leftchild
    def leftchild(self,pos):
        return pos * 2

    # rightchild
    def rightchild(self,pos):
        return (pos * 2) + 1

    # isleaf
    def isLeaf(self,pos):
        return (pos * 2) > self.size
    
    #swap
    def swap(self,indexA,indexB):
        self.Heap[indexA],self.Heap[indexB] = self.Heap[indexB],self.Heap[indexA]
    
    def minHeapify(self,pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[self.leftchild(pos)] or self.Heap[pos] > self.Heap[self.rightchild(pos)]:
                if self.Heap[self.leftchild(pos)] < self.Heap[self.rightchild(pos)]:
                    self.swap(pos,self.leftchild(pos))
                    self.minHeapify(self.leftchild(pos))
                else:
                    self.swap(pos,self.rightchild(pos))
                    self.minHeapify(self.rightchild(pos))
    
    #insert
    def insert(self,element):
        if self.size >= self.maxsize:
            return
        
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)
    
    #delete
    def delete(self,pos=None):
        if pos:
            popped = self.Heap[pos]
            self.Heap[pos] = self.Heap[self.size]
            self.size -= 1
            self.minHeapify(pos)
            return popped
        else:
            #delete from root
            popped = self.Heap[self.FRONT]
            self.Heap[self.FRONT] = self.Heap[self.size]
            self.size -= 1
            self.minHeapify(self.FRONT)
            return popped

    
    #create minheap
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
    
    #Print
    def Print(self):
        print(self.Heap)
        #parents in Heap
        # for i in range(1, (self.size//2) + 1):
        #     print(self.Heap[i],end=" ")
    

    
print('The minHeap is ')
minHeap = MinHeap(15)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.minHeap()
 
print("The Min val is " + str(minHeap.delete(2)))
minHeap.Print()