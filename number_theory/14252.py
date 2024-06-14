N = int(input())
arr = list(map(int, input().split()))

arr.sort()


def _gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b


count = 0
arr2 = []

for i in range(0, N - 1):
    if _gcd(arr[i], arr[i + 1]) > 1:
        arr2.append([arr[i], arr[i + 1]])

for a, b in arr2:
    for j in range(a + 1, b):
        tmp = 0
        if _gcd(a, j) == 1 and _gcd(b, j) == 1:
            count += 1
            break

        if j == (b - 1):
            count += 2

print(count)
