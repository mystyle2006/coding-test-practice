A, B = map(int, input().split())
A -=1
temp_a = A
for i in range(1, 50):
    temp_a += (A // 2 ** i) * (2 ** (i - 1))

temp_b = B
for i in range(1, 50):
    temp_b += (B // 2 ** i) * (2 ** (i - 1))

print(temp_b - temp_a)
