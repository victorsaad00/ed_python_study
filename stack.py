class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = int(0)

    def push(self, data):

        node = Node(data)
        if self.isEmpty():
            self.top = node
            self.size += 1

        else:
            aux = node
            aux.next = self.top
            self.top = aux
            self.size += 1
    
    def pop(self):

        if self.isEmpty():
            return

        else:
            #value = self.top.data
            self.top = self.top.next
            self.size -= 1
            #return value

    def isEmpty(self):
        return self.size == 0

    def whoIsTop(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data
