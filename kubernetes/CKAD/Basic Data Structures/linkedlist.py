# 1 -> 2 -> 3
# reverse
# search
# add at particular index or node
class Node():
    def __init__(self,data):
        self.key = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def insertAtIndex(self,index,data):
        temp = self.head
        while index > 0 and temp.next != None:
            temp = temp.next
            index -= 1
        if(index == 0):
            newNode = Node(data)
            if temp.next == None:
                temp.next = newNode
            else:
                next = temp.next
                temp.next = newNode
                newNode.next = next
            return "Added"
        return "Index Not Available"

    def search(self,data):
        temp = self.head
        while temp.next != None:
            if temp.key == data:
                return "Found"
            temp = temp.next
        if temp.key == data:
            return "Found"
        return "Not Found"

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
    
    def pushFront(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            prevHead = self.head
            self.head = newNode
            newNode.next = prevHead
    
    def pushBack(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = newNode
    
    def Print(self):
        if self.head != None:
            temp = self.head
            while temp.next != None:
                print(temp.key,end=" ")
                temp = temp.next
            print(temp.key)

head = LinkedList()
head.pushFront(1)
head.pushFront(2)
head.pushFront(3)
# head.reverse()
head.Print()

head1 = LinkedList()
head1.pushBack(1)
head1.pushBack(2)
head1.pushBack(3)
# print(head1.insertAtIndex(2,10))
head1.Print()
# print(head1.search(3))

