import sys

sys.setrecursionlimit(999999)

N, M = map(int, input().split())

arr = []


def recur(idx):
    if idx == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if i in arr:
            continue

        arr.append(i)
        recur(idx + 1)
        arr.pop()


recur(0)
