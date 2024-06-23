N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(N + 1)]


# dfs
def dfs(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue

        dfs(nxt)


dfs(1)
print(sum(visited) - 1)
