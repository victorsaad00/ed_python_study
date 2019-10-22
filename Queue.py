class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None

class Queue:

    def __init__(self):

        self.first = None
        self.last = None
        self.size = 0

    def inqueue(self, data):

        node = Node(data) # create new node
        if self.isEmpty():
            self.first = node
            self.last = node
            self.size += 1

        else:
            self.last.next = node
            self.last = node
            self.size += 1

    def dequeue(self):

        if self.isEmpty():
            print('Queue is empty!')
            return None

        else:
            first_data = self.first.data

            if self.first is self.last:
                self.first = None
                self.last = None
                self.size -= 1
            
            else:
                self.first = self.first.next
                self.size -= 1

            return first_data
            
    def isEmpty(self):
        return self.size == 0
