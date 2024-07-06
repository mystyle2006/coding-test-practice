import heapq

N,M = map(int,input().split())
start = int(input())
links = [[] for _ in range(N+1)]
dist = [1e9 for _ in range(N+1)]

for _ in range(M):
    FROM,TO,WEIGHT = map(int,input().split())
    links[FROM].append([TO, WEIGHT])

# bfs!

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    _w, node = heapq.heappop(q)

    for nxt, weight in links[node]:
        # 1. 각각의 위치에 값을 업데이트
        # 2. 만약에 여러 경로가 있다면 min 비교!
        # 3. 시작점으로부터 거리를 봐서 짧은 순서대로 탐색!
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

for _d in dist[1:]:
    print("INF" if _d == 1e9 else _d)