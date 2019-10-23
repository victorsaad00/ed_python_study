# My queue implemented with Dijkstra algorythm without using dictionary.
# I didn't use dictionary for learning/exercices proporses.

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

def dijkstra(graph, orig_vert, len_dist):

    # The index is the vertice and the values are the distances.
    # distance = [0, inf, inf, ... , inf] if orig_vert is equal to first vertice. 
    distance = [float('inf')] * len_dist 
    distance[orig_vert-1] = 0  
    
    q = Queue()
    # Queue a tuple, (vertice, distance of that vertice). 
    q.inqueue((orig_vert, distance[orig_vert-1])) 

    while not q.isEmpty():
        # deQueue a tuple = (vertice, distance)
        t = q.dequeue() 
        vertice = t[0] 
        min_vertice_distance = t[1]

        if min_vertice_distance == distance[vertice-1]:
                
            # v is every adjacent of vertice.
            for v in graph[vertice-1]:
                vert = v[0]
                vert_dist = v[1]

                if distance[vertice-1] + vert_dist < distance[vert-1]:
                    distance[vert-1] = distance[vertice-1] + vert_dist
                    q.inqueue((vert, distance[vert-1]))

    return distance
