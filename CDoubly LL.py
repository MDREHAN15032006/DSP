class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def createCDLL(self,value):
        new_node=Node(value)
        new_node.next=None
        new_node.prev=None
        self.head=new_node
        self.tail=new_node
        print("The circular doubly linked list has been created.")

    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        last_node=self.head
        while(last_node.next !=self.head):
            last_node=last_node.next
        last_node.next=new_node
        new_node.prev=last_node
        self.tail=new_node
        self.tail.next=self.head
        self.head.prev=self.tail

    def insertAtBeg(self,value):
        new_node=Node(value)
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
        self.tail.next=self.head
        self.head.prev=self.tail

    def delBeg(self):
        if(self.head==None):
            return
        elif(self.head.next==self.tail.next):
            self.head=self.tail=None
            return
        elif(self.head is not None):
            next_node=self.head.next
            next_node.prev=None
            self.head=next_node
            self.tail.next=self.head
            self.head.prev=self.tail
            return

    def searchList(self,value):
        position=0
        found=0
        if self.head is None:
            print("The linked list does not exist")
        else:
            temp_node=self.head
            while temp_node:
                position=position+1
                if temp_node.value==value:
                    print("The required value was found at position: "+str(position))
                    found=1
                    break
                if temp_node==self.tail:
                    print("the required value does not exist in the list")
                    break
                temp_node=temp_node.next

    def Display(self):
        if self.head==None:
            print("The linked list does not exist.")
        else:
                temp_node=self.head
                while temp_node:
                    print(temp_node.value)
                    if temp_node==self.tail:
                        break
                    temp_node=temp_node.next

CDLL=CDoublyLinkedList()
CDLL.createCDLL(10)
CDLL.insertAtBeg(20)
CDLL.insertAtEnd(30)
CDLL.insertAtEnd(40)
CDLL.insertAtEnd(50)
CDLL.insertAtEnd(60)
print("List contents are:")
CDLL.Display()
CDLL.delBeg()
CDLL.delBeg()
print("List contents after deleting:")
CDLL.Display()
CDLL.searchList(7)
CDLL.searchList(60)
