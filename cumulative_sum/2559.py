N, K = map(int, input().split())
values = list(map(int, input().split()))

prefix = [0 for _ in range(N+2)]
for i in range(0, N):
    prefix[i + 1] = prefix[i] + values[i]

answer = []
for j in range(K, N + 1):
    answer.append(prefix[j] - prefix[j - K])


print(max(answer))
