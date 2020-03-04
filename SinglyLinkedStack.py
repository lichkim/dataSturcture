#Single Linked List

#Node class
class Node:
    
    #initial method
    def __init__(self, data, next):
        self.data=data
        self.next=next
        
        pass
    
    def setNextNode(self, node):
        self.next=node
        
        pass
    
    def setData(self, data):
        self.data=data
        
        pass
    
    def getNextNode(self):
        return self.next

    def getData(self):
        return self.data
    
    pass
    

#SinglyLinkedList class
class SinglyLinkedList:

    #initial method
    def __init__(self):
        self.head=None
        self.tail=None
        self.__size=0
        
        pass

    #method that determines whether the list is empty or not
    def isEmpty(self):
        return self.__size==0
    
    #method that returns size of the list
    def size(self):
        return self.__size

    #method that returns the data at First node
    def Top(self):
        return self.head.getData()
    
    #method that returns node at index idx
    def node(self, idx):
        temp=head
        
        for i in range(idx):
            temp=temp.getNextNode()
        
        return temp

    #method to add new node at the first of the list
    def addFirst(self, data):
        newNode=Node(data,None)
        newNode.setNextNode(self.head)
        self.head=newNode
        self.__size+=1
        
        if newNode.getNextNode()==None:
            tail=newNode
        
        pass

    #method to add node at index idx
    def add(self, data, idx):
        if idx==0:
            addFirst(data)
        else:
            prev=self.node(idx-1)
            newNode=Node(data, prev.getNextNode())
            prev.setNextNode(newNode)
            self.__size+=1
            if newNode.getNextNode()==None:
                tail=newNode
        
        pass
    
    #method to remove the Top node of the list. + returns the data at it.
    def removeFirst(self):
        toRemove=self.head
        self.head=self.head.getNextNode()
        returnData=toRemove.getData()
        toRemove=None
        self.__size-=1
        return returnData

    #method to remove node at idx. + returns the data at it.
    def remove(self, idx):
        if idx==0:
            return removeFirst()
        else:
            prev=self.node(idx-1)
            toRemove=prev.getNextNode()
            prev.setNextNode(prev.getNextNode().getNextNode())
            returnData=toRemove.getData()
            toRemove=None
            self.__size-=1
            return returnData
    
    pass


'''
Stack class
Stack is a kind of data structure that forms like a box that has blocked floor
For example, if you put 1, 2, 3, 4, 5, 7, 9 in a stack, the stack is like below:

|9|
|7|
|5|
|4|
|3|
|2|
|1|
---

These 'putting' is called 'push'

and if you get data from stack, then you can get data from Top to Floor. As the example above, you can get:

9 7 5 4 3 2 1
    
These 'getting data' is called 'pop'. If the stack is empty, usually it returns -1 for exception

'Size' method is a method that returns the number of data in the stack

'Empty' method is a method that tells whether the stack is empty or not

'Top' method is a method that returns the data at the top of the stack. If the stack is empty, it usually returns -1 for exception

The most important and distict characteristic of stack is 'LIFO', which stands for 'Last In, First Out', or, 'FILO', which stands for 'First In, Last Out'

You can make stack in both array and linked list. In this source, Singly Linked List is used
'''

#Stack class
class Stack:
    
    #initial method
    def __init__(self):
        self.datalist=SinglyLinkedList()
        pass
    
    #size method. It returns the size of the list
    def size(self):
        return self.datalist.size()
    
    #isEmpty method. It determines whether the list is empty or not
    def isEmpty(self):
        return self.datalist.isEmpty()
    
    #Top method. It returns the data at the top of the stack
    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.datalist.Top()

    #push method. It inputs the data in list
    def push(self, data):
        self.datalist.addFirst(data)
        pass

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.datalist.removeFirst()
    
    pass


#This is an example of https://www.acmicpc.net/problem/10828
#With this code, time runs out, but still works

if __name__=='__main__':
    stack=Stack()
    N=int(input())

    for i in range(N):
        buffer=input()
        
        if 'push' in buffer:
            strarr=buffer.split()   
            data=int(strarr[-1])
            stack.push(data)
        
        elif 'pop' in buffer:
            print(stack.pop())
        
        elif 'size' in buffer:
            print(stack.size())
        
        elif 'empty' in buffer:
            if stack.isEmpty():
                print(1)
            else:
                print(0)
        
        elif 'top' in buffer:
            print(stack.top())
