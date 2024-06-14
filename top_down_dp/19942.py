WEIGHT = 0
VALUE = 1


def recur(idx, weight):
    if weight > B:
        return -999999999

    if idx == N:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 담았을 때
    dp[idx][weight] = max(recur(idx + 1, weight + things[idx][WEIGHT]) + things[idx][VALUE], recur(idx + 1, weight))

    return dp[idx][weight]


N, B = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100_001)] for _ in range(N + 1)]

answer = recur(0, 0)

print(answer)
