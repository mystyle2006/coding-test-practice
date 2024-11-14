N = int(input())
graph = [[] for _ in range(N+1)]
par = [0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def recur(node, prev):
    par[node] = prev

    for nxt in graph[node]:
        if nxt == prev:
            continue
        recur(nxt, node)

recur(1, 0)

print(par)