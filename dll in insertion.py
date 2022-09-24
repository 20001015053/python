class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class dlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def creatdll(self,data):
        newnode=Node(data)
        newnode.prev=None
        newnode.next=None
        self.head=newnode
        self.tail=newnode
        return "dll is created" 
    def insertion(self,nodevalue,location):
        newnode=Node(nodevalue)
        if location==0:
            newnode.prev=None
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        if location==1:
            newnode.next=None
            newnode.prev=self.tail
            self.tail.next=newnode
            self.tail=newnode
dll=dlist()
dll.creatdll(4)
print([node.value for node in dll])
dll.insertion(3,0)
dll.insertion(5,1)
print([node.value for node in dll])