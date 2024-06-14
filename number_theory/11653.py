N = int(input())

_N = N
i = 2
answer = []


def isPrime(a):
    result = True
    for j in range(1, a):
        if j != 1 and a % j == 0:
            result = False
    return result


while True:
    if _N % i == 0:
        _N = _N / i
        if isPrime(i):
            print(i)
    else:
        i += 1

    if _N == 1:
        break

