from collections import deque

y, x = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(y)]

# dfs
max_dist = 0

for _y in range(y):
    for _x in range(x):
        if maps[_y][_x] != 'L':
            continue

        visited = [[0 for _ in range(x)] for _ in range(y)]
        dist = [[0 for _ in range(x)] for _ in range(y)]

        q = deque()
        q.append([_y, _x])
        visited[_y][_x] = 1

        while len(q) > 0:
            ey, ex = q.popleft()

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = ey + dy, ex + dx
                # 범위 체크
                if 0 <= ny < y and 0 <= nx < x:
                    # 방문을 안했고 땅이라면
                    if visited[ny][nx] != 1 and maps[ny][nx] == 'L':
                        dist[ny][nx] = dist[ey][ex] + 1
                        visited[ny][nx] = 1
                        q.append([ny, nx])
                        max_dist = max(max_dist, dist[ny][nx])

print(max_dist)


