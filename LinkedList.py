class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
    def __repr__(self):
        return self.data

class LinkedList:
    len = 0
    def __init__(self):
        self.head = None
    def get(self,pos):
        if pos > self.len or pos < 0:
            raise Exception('index out of range')
        n = self.head
        while n is not None:
            if pos == 0:
                return n
            pos -= 1
            n = n.next
    def push(self, node):
        n = self.head
        self.len += 1
        if n == None:
            self.head = node
            return
        while n.next is not None:     
            n = n.next
        n.next = node
    def unshift(self,node):
        node.next = self.head
        self.head = node
        self.len += 1
    def pop(self):
        if self.head == None:
            raise Exception('the list is empty')
        self.len -= 1
        if self.head.next == None:
            self.head = None
            return
        n = self.head
        lastItem = n
        while n.next is not None:     
            lastItem= n
            n = n.next
        lastItem.next = None
    def shift(self): 
        if self.head == None or self.head.next == None:
            self.head = None
            self.len = 0
            return
        self.len -= 1
        self.head = self.head.next
    def insert(self, node,pos):
        if pos == 0:
            self.unshift(node)
            return
        n = self.head
        current = None
        while(pos > 0):
            pos-=1
            current = n
            n = n.next
        current.next = node
        node.next = n    
        self.len += 1
    def clear(self):
        self.head = None
        self.len = 0
        return True    
    def remove(self,pos):
        pass
    def replace(self,pos):
        pass
    def reverse(self):
        pass
    def sort(self):
        pass
    def asort(self):
        pass
    def toList(self):
        pass
    def __repr__(self):
        l = []
        node = self.head
        while node is not None:
            l.append(node.data)
            node = node.next
        l.append("None")
        return " -> ".join(l)
linkedList = LinkedList()
linkedList.push(Node("0"))
linkedList.push(Node("1"))
linkedList.push(Node("2"))
linkedList.push(Node("3"))
print(linkedList.len)
print(linkedList)