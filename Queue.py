class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class Stack:
    len = 0
    def __init__(self, my_list = None):
        self.head = None
    def push(self, node):
        pass
    def pop(self):
        pass
    def clear(self):
        pass
    def peekTop(self):
        pass
    def peekBottom(self):
        pass
    def __repr__(self):
        l = []
        n = self.head
        while n is not None:
            l.append(n.data)
            n = n.next
        l.append(None)
        return " -> ".join(map(str, l))
