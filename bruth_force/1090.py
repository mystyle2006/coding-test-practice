n = int(input())
arr = []
arr_y = []
arr_x = []
answer = [-1] * n

for i in range(n):
    xy = list(map(int, input().split()))
    arr.append(xy)
    arr_y.append(xy[0])
    arr_x.append(xy[1])

for y in arr_y:
    for x in arr_x:
        dist = []
        for ey, ex in arr:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)

        dist.sort()

        temp = 0
        for i in range(len(arr)):
            temp += dist[i]

            if answer[i] == -1:
                answer[i] = temp
            else:
                answer[i] = min(answer[i], temp)

print(*answer)
