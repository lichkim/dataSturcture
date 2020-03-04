#Doubly Linked List

#Node class
class Node:
    
    #initial method
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
        
        pass
    
    def setNextNode(self, node):
        self.next=node
        pass
    
    #This method is only for doubly linked list. It sets the previous node
    def setPrevNode(self, node):
        self.prev=node
        pass
    
    def setData(self, data):
        self.data=data
        pass
    
    def getNextNode(self):
        return self.next
    
    #This method is also only for doubly linked list. It gets the previous node
    def getPrevNode(self):
        return self.prev

    def getData(self):
        return self.data
    
    pass

class DoublyLinkedList:
    #initial method
    def __init__(self):
        self.head=None
        self.tail=None
        self.__size=0
    
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size()==0
    
    def __node(self, idx):
        #search from the start(head)
        if idx<self.__size/2:
            temp=self.head
            for i in range(idx):
                temp=temp.getNextNode()
            return temp
        #search from the end(tail)
        else:
            temp=self.tail
            for i in range(self.__size-1-idx):
                temp=temp.getPrevNode()
            return temp

    def addFirst(self, data):
        newNode=Node(data)
        newNode.setNextNode(self.head)

        if self.head!=None:
            self.head.setPrevNode(newNode)
        
        self.head=newNode
        self.__size+=1

        if self.head.getNextNode()==None:
            self.tail=self.head

        pass

    def addLast(self, data):
        newNode=Node(data)

        if self.isEmpty():
            self.addFirst(data)
        else:
            tail.next=newNode
            newNode.setPrevNode(self.tail)
            self.tail=newNode
            self.__size+=1
        
        pass

    def add(self, data, idx):
        if idx==0:
            self.addFirst(data)
        elif idx==self.__size-1:
            self.addLast(data)
        else:
            prev=self.__node(idx-1)
            next=prev.getNextNode()
            newNode=Node(data)
            prev.setNextNode(newNode)
            
            if next!=None:
                next.setPrevNode(newNode)
            
            newNode.setNextNode(next)
            newNode.setPrevNode(prev)

            self.__size+=1

            #newNode is the last node
            if newNode.getNextNode()==None:
                self.tail=newNode
        
        pass

    def removeFirst(self):
        if self.isEmpty():
            return -1
        else:
            toRemove=self.head
            self.head=self.head.getNextNode()
            data=toRemove.getData()
            toRemove=None

            if self.head!=None:
                self.head.setPrevNode(None)
            
            return data

    def removeLast(self):
        if self.__size==0:
            self.removeFirst()
        else:
            prev=
