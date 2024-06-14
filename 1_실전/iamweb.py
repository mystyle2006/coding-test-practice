# 22 % 9 != 0
# 222222222222222222 % 9

def find_min_repeats(n, k):
    current_number = 0
    for i in range(1, 10001):  # 최대 10000번 반복
        current_number = current_number * 10 + n
        current_number %= k
        if current_number == 0:
            return i
    return -1

print(find_min_repeats(22, 9))
print(find_min_repeats(25, 15))