WEIGHT = 0
VALUE = 1


def recur(idx, weight, value):
    global answer

    if weight > B:
        return

    if idx == N:
        answer = max(answer, value)
        return

        # 물건을 담았을 때
    recur(idx + 1, weight + things[idx][WEIGHT], value + things[idx][VALUE])
    # 물건을 안담았을 때
    recur(idx + 1, weight, value)


N, B = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]

answer = 0

recur(0, 0, 0)

print(answer)