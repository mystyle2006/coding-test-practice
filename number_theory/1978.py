N = int(input())
numbers = list(map(int, input().split()))

primes = 0
for i in range(0, N):
    if numbers[i] == 1:
        continue

    isPrime = True
    for j in range(1, numbers[i]):
        if j != 1 and numbers[i] % j == 0:
            isPrime = False

    if isPrime:
        primes += 1

print(primes)