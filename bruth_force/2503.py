N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for a in range(1, 10):  # 100의 자리수
    for b in range(1, 10):  # 10의 자리수
        for c in range(1, 10):  # 1의 자리수
            if a == b or b == c or c == a:
                continue

            cnt = 0
            for arr in hint:
                number = str(arr[0])
                strike = arr[1]
                ball = arr[2]

                _strike = 0
                _ball = 0

                for j in range(3):
                    # j번째 자리수가 같다면 스트라이크
                    if int(number[j]) == [a, b, c][j]:
                        _strike += 1
                    # 자리수는 다르지만 있다면 볼
                    elif int(number[j]) in [a, b, c]:
                        _ball += 1

                if strike == _strike and ball == _ball:
                    cnt += 1

            if cnt == N:
                answer += 1

print(answer)