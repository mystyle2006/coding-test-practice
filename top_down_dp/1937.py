import sys

sys.setrecursionlimit(1000000)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
answer = 0


def recur(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    # 방문
    dp[y][x] += 1

    for dy, dx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ex = x + dx
        ey = y + dy

        if 0 <= ex < n and 0 <= ey < n:
            if forest[y][x] < forest[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)

    return dp[y][x]


for y in range(n):
    for x in range(n):
        recur(y, x)

print(max(map(max, dp)) + 1)
