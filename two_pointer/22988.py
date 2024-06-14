N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

p1 = 0
p2 = N - 1
cnt = 0
remain = 0

while p1 <= p2:
    if arr[p2] == X:
        cnt += 1
        p2 -= 1
        continue

    if p1 == p2:
        remain += 1
        break

    if (arr[p1] + arr[p2]) >= X/2:
        cnt += 1
        p1 += 1
        p2 -= 1
    else:
        remain += 1
        p1 += 1

print(cnt + (remain // 3))

