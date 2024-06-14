N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def recur(idx, value):
    global answer
    if idx >= N:
        if idx > N:
            return

        answer = max(answer, value)
        return

    recur(idx + consult[idx][0], value + consult[idx][1])
    recur(idx + 1, value)


recur(0, 0)
print(answer)
