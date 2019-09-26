def DFS(graph, visited, v, path):

    visited[v-1] = True
    path.append(v)

    for adj in graph[v]:
        if visited[adj-1] is not True:
            DFS(graph, visited, adj, path)

def main(graph, v):

    visited = [False] * len(graph)

    path = []
    DFS(graph, visited, v, path)
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

main(graph, 1)