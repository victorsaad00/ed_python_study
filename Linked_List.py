# Not finished



class Node(object):

    def __init__(self):
        self.data = None
        self.next = None


class List:   # Simple linked list

    def __init__(self):
        self.cur_node = None
        self.size = 0

    #####################
    '''
    # Only for ordered list
    def insertFirst(self, data):
        pass
    
    def insertNext(self, data):
        pass
        
    def deleteMid(self, data):
        pass

    def deleteLast(self,data):
        pass

    def deleteFirst(self, data):
        pass
    '''
    ######################

    def insert(self, data):
        new_node = Node()  # create a new node
        new_node.data = data
        new_node.next = self.cur_node  # link the new node to the 'previous' node.
        self.cur_node = new_node  # set the current node to the new one.
        self.size += 1

    def list_print(self):
        node = self.cur_node  # cant point to ll!
        while node:
            print(str(node.data))
            node = node.next

    def delete(self, data):
        if not self.isEmpty():
            if self.exist_rec(data, self.cur_node):
                pass # Search node, unlink it and link the prev with the next.
        else:
            print('List is empty!')

    def exist(self, data):
        node = self.cur_node
        while node:
            if node.data == data: return True
            else: node = node.next
        return False

    def exist_rec(self, data, node):
        if self.isEmpty(): return False
        elif node.data == data: return True
        else: return self.exist_rec(data, node.next)

    def isEmpty(self):
        return self.size == 0






