N = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

p1 = 0
p2 = len(arr) - 1
cnt = 0

while p1 < p2:
    if arr[p1] + arr[p2] == x:
        cnt += 1

    if arr[p1] + arr[p2] >= x:
        p2 -= 1
    else:
        p1 += 1

print(cnt)
