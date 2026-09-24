n = int(input("Enter number of users: "))

matrix = [[0 for _ in range(n)] for _ in range(n)]
adj_list = {i: [] for i in range(n)}

edges = int(input("Enter number of connections: "))

print("\nEnter connection (user1, user2):")

for _ in range(edges):
    u, v = map(int, input().split())

    matrix[u][v] = 1
    matrix[v][u] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)

print("\n--- ADJACENCY MATRIX ---")
print("  ", end="")

for i in range(n):
    print(i, end=" ")

print()

for i in range(n):
    print(i, end=". ")

    for j in range(n):
        print(matrix[i][j], end=" ")

    print()

print("\n--- ADJACENCY LIST ---")

for user in adj_list:
    print(user, "->", adj_list[user])


print("\n--- CONNECTION CHECK ---")

a, b = map(
    int,
    input("Enter two users to check: ").split()
)

if matrix[a][b] == 1:
    print(f"Users {a} and {b} are directly connected.")
else:
    print(f"Users {a} and {b} are not directly connected.")

print("\n--- USER DEGREE ---")

for user in adj_list:
    print(f"User {user}: {len(adj_list[user])} connection(s)")
