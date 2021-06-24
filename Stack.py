class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class Stack:
    len = 0
    def __init__(self):
        self.head = None
    def push(self, node):
        self.len+=1
        node.next = self.head
        self.head = node
    def pop(self):
        self.len-=1
        if self.head is None:
            raise Exception('Empty stack')
        self.head = self.head.next
    def peek(self):
        return self.head
    def clear(self):
        self.len = 0
        self.head = None
    def __repr__(self):
        l = []
        n = self.head
        while n is not None:
            l.append(n.data)
            n = n.next
        l.append(None)
        return " -> ".join(map(str, l))

stack = Stack()
stack.push(Node('1'))
stack.push(Node('2'))
print(stack)