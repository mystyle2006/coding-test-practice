K = int(input())
j = []
for i in range(2, int(K ** 0.5) + 1):
    while K % i == 0:
        j.append(i)
        K = K // i

if K != 1: j.append(K)

print(len(j))
print(*j)
