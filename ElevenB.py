graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges:"))
print("Enter edges (source destination):")
for i in range(e):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("\nEnter starting vertex:"))

def BFS(start):
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result

def DFS(start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return result
print("\n---GRAPH---")
for vertex in graph:
    print(vertex, "->", graph[vertex])
print("\nBFS Traversal:", *BFS(start))
print("DFS Traversal:", *DFS(start))
