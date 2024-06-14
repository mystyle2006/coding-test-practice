import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 누적 합
prefix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        prefix[y + 1][x + 1] = prefix[y + 1][x] + prefix[y][x + 1] - prefix[y][x] + graph[y][x]

for _ in range(M):
    y, x, y1, x1 = map(int, input().split())
    answer = prefix[y1][x1] - prefix[y - 1][x1] - prefix[y1][x - 1] + prefix[y - 1][x - 1]
    print(answer)
