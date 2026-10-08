INF = 9999

def dijkstra(graph, source, destination):
    n = len(graph)
    distance = [INF] * n
    visited = [False] * n
    previous = [-1] * n

    distance[source] = 0

    for _ in range(n):
        u = -1
        minimum = INF

        for i in range(n):
            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    previous[v] = u

    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = previous[current]
    path.reverse()

    if distance[destination] == INF:
        print("No path exists")
    else:
        print("\nShortest Path : ", end="")
        for node in path:
            print(chr(65 + node), end=" ")
        print("\nShortest Distance :", distance[destination])
n = int(input("Enter number of cities: "))

print("Enter adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

print("\nCities are:")
for i in range(n):
    print(i, "->", chr(65 + i))

source = ord(input("\nEnter source city: ").upper()) - 65
destination = ord(input("Enter destination city: ").upper()) - 65

dijkstra(graph, source, destination)
