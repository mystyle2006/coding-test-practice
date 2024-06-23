from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(N + 1)]


# bfs
q = deque()
q.append(1)

while len(q) > 0:
    node = q.popleft()
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue

        q.append(nxt)

print(sum(visited) -1)