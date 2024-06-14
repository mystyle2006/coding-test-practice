import sys
input = sys.stdin.readline

N, H = map(int, input().split())
line = [0 for _ in range(H)]

for t in range(N):
    height = int(input())
    # 석순(바닥에서 자라는 것)
    if t % 2 == 0:
        line[0] += 1
        line[height] -= 1

    # 종유석 (천장에서 자라는 것)
    if t % 2 == 1:
        line[H - height] += 1

prefix = [0 for _ in range(H + 1)]
for i in range(H):
    prefix[i + 1] = prefix[i] + line[i]

prefix = prefix[1:]
print(min(prefix), prefix.count(min(prefix)))
