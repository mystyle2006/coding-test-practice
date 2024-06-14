N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]
dp = [-1e9 for _ in range(N + 1)]


def recur(idx):
    if idx >= N:
        if idx > N:
            return -1e9
        return 0

    if dp[idx] >= 0:
        return dp[idx]

    print(f'dp[{idx}] = max(recur({idx + consult[idx][0]}) + consult[{idx}][1], recur({idx + 1})) = {max(recur(idx + consult[idx][0]) + consult[idx][1], recur(idx + 1))}')
    dp[idx] = max(recur(idx + consult[idx][0]) + consult[idx][1], recur(idx + 1))
    return dp[idx]


recur(0)
print(dp)
