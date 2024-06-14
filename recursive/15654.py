import sys

sys.setrecursionlimit(99999999)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []


def recur():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(0, N):
        if numbers[i] in arr:
            continue

        arr.append(numbers[i])
        recur()
        arr.pop()


recur()
