import sys

sys.setrecursionlimit(999999)

N, M = map(int, input().split())

arr = []


def recur(idx):
    if idx == M:
        is_asc = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_asc = False
                break
        if is_asc: print(*arr)
        return

    for i in range(1, N + 1):
        if i in arr:
            continue

        arr.append(i)
        recur(idx + 1)
        arr.pop()


recur(0)
