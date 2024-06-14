import sys

sys.setrecursionlimit(1000000)

M, N = map(int, input().split())
paths = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]


def recur(y, x):
    if y == M - 1 and x == N - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    route = 0
    for dy, dx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ex = x + dx
        ey = y + dy

        if 0 <= ex < N and 0 <= ey < M:
            if paths[y][x] > paths[ey][ex]:
                route += recur(ey, ex)

    dp[y][x] = route
    return dp[y][x]


recur(0, 0)

for i in dp:
    print(i)
print(recur(0, 0))