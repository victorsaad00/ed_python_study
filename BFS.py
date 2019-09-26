def BFS(graph, queue, visited, v, path):

    visited[v-1] = True
    vert = queue.pop()
    path.append(vert)

    for adj in graph[vert]:

        if visited[adj-1] is False:

            queue.append(adj)
            BFS(graph, queue, visited,adj, path)



def main(graph, v):

    visited = [False] * len(graph)
    queue = []
    path = []

    queue.append(v)
    BFS(graph, queue, visited, v, path)
    print(path)



graph = {
    1:[2,4],
    2:[1,3,8,7,5],
    3:[2,4,10,9],
    4:[1,3],
    5:[2,7,6],
    6:[5],
    7:[5,2,8],
    8:[2,5,7],
    9:[3],
    10:[3]
}
main(graph, 5)