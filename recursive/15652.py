import sys

sys.setrecursionlimit(99999999)

N, M = map(int, input().split())

arr = []


def recur(idx):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(idx, N + 1):
        arr.append(i)
        recur(i)
        arr.pop()


recur(1)
