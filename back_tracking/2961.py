N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9


def recur(idx, sour, bitter, use):
    global answer
    if idx == N:
        if use > 0:
            answer = min(answer, abs(sour - bitter))
        return

    recur(idx + 1, sour * ingredient[idx][0], bitter + ingredient[idx][1], use + 1)
    recur(idx + 1, sour, bitter, use)


recur(0, 1, 0, 0)
print(answer)