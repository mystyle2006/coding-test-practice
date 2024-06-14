# 당신은 TFT(Ticket Finding Tactics) 라는 게임을 플레이하고 있습니다.
# 이 게임은 주어진 황금 티켓을 최대한 많이 모우는 것입니다
#
# 당신이 이 게임에서 할 수 있는 행동은 다음과 같습니다.
# - 상점에서 일반 티켓 구매하기
# - 상점 새로고침하기
# - 동일한 일반 티켓 3개를 황금 티켓 1개로 교환하기
#
# 상점에는 일반 티켓 m개가 진열되어 있습니다. 당신은 티켓의 가격을 지불하여 진열되어 있는 티켓 중 원하는 티켓으로 구매할 수 있습니다.
# 또, 일정 금액을 상점에 지불하고 상점을 최대 n - 1 번 새로고침 할 수 있습니다. 새로고침이란, 상점에 진열 중이던 티켓을 모두 폐기하고
# 새로운 일반 티켓 m 개를 진열하는 행동입니다.

# 당신은 상점에 진열되는 티켓의 패턴을 분석하여 상점을 새로고침 했을 때 매번 어떤 티켓이 진열될지 예측하는데 성공했습니다. 당신은 예측한 결과를 바탕으로
# 황금 티켓을 가장 많이 모을 수 있는 방법으로 자금을 사용하려 합니다.

# 다음은 상점에서 티켓을 구매하여 황금 티켓을 모으는 예시입니다.
# <일반 티켓의 종류>
# 티켓 이름, 가격
# A        1
# B        2
# C        5
# D        3

# <상점의 티켓 진열 예측>
# 최초 상점    B,C,B,C
# 두 번째 상점 A, A, A, B
# 세 번째 상점 D, D, C, D

# 일반 티켓의 종류와 상점의 티켓 진열 패턴이 위 표와 같고, 상점 새로고침에 필요한 금액이 10, 당신에게 주어진 자금이 30이라고 가정해봅시다. 최초 상점에서
# "B" 2개를 구매하고, 새로고침 한 뒤, 두 번째 상점에서 "A" 3개, "B" 1개를 구매하면 총 2 * 2 + 10 + 1 * 3 + 2 * 1 = 19 만큼 자금을 사용해
# "A" 3개, "B" 3개를 구매할 수 있습니다. "A" 3개, "B" 3개를 황금 티켓을 2개로 교환할 수 있으며, 이보다 더 많은 황금 티켓을 모으는 방법은 없습니다.

# 게임에 등장하는 모든 일반 티켓의 정보가 담긴 문자열 배열 tickets, 상점 새로고침에 필요한 금액을 나타내는 정수 roll, 상점의 새로고침 예측이 담긴 2차원 문자열 배열 shop과
# 당신에게 주어진 자금을 나타내는 정수 money 가 매개변수로 주어집니다.

# 이때 모을 수 있는 황금 티켓 개수의 최댓값을 return 하도록 solution 함수를 완성해주세요.

# 1 <= tickets 의 길이 <= 1000
# tickets 의 원소는 "TICKET_NAME TICKET_PRICE" 형태입니다.
# - TICKET_NAME은 티켓의 이름을 나타내고, 알파벳 대문자로만 구성된 길이 1~10 사이인 문자열입니다.
# - TICKET_PRICE는 티켓의 가격을 나타내며, 1 ~ 10000 사이의 숫자입니다.
# - TICKET_NAME(티켓의 이름)이 중복된 입력은 주어지지 않습니다.

# 1 <= roll <= 1000
# 1 <= shop의 길이 = n <= 1000
# - shop[i] 는 새로고침을 i번 했을 때 상점에 진열되는 티켓들의 이름을 담고 있습니다.
# - 0 <= i <= n - 1
# - shop 의 길이 이상 새고로침 할 수는 없습니다.
# - 1 <= shop[i] 의 길이 = m <= 100
# -- tickets 에 나타난 티켓의 이름만 담겨있습니다.
# 1 <= money <= 100,000,000

# 입출력 예
# tickets | roll | shop | money | result
# ["A 1", "B 2", "C 5", "D 3"] | 10 | [["B", "C", "B", "C"],["A", "A", "A", "B"], ["D", "D", "C", "D"]] | 30 | 2
# ["A 1", "B 2", "C 5", "D 3"] | 10 | [["B", "C", "B", "C"],["A", "A", "A", "B"], ["D", "D", "C", "D"]] | 100 | 4
# ["A 2", "B 1"] | 1 | [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]] | 9 | 2
# ["A 2", "B 1"] | 5 | [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]] | 19 | 2

# 입출력 예 #1
# 문제 예시와 같습니다
# 입출력 예 #2
# 처음 주어진 자금인 money 가 두 번의 새로고침 비용과 모든 티켓 비용을 지불하고도 남을 만큼 충분합니다. 따라서 상점에 등장하는 모든 티켓을 구매하면, 황금 티켓 4개를 모을 수 있습니다.
# 입출력 예 #3
# 다음과 같은 방법으로 황금 티켓 2개를 모을 수 있으며, 이보다 더 많은 황금 티켓을 모을 수 있는 방법이 없습니다.
# 1. 첫 번째 상점에서 티켓을 구매하지 않고 새로고침 합니다.
# 2. 두 번째 상점에서 "B" 2개를 구매하고 새로고침 합니다.
# 3. 세 번째 상점에서 "B" 2개를 구매하고 새로고침 합니다.
# 4. 네 번째 상점에서 "B" 2개를 구매합니다.
# 5. "B" 6개를 황금 티켓 2개와 교환할 수 있습니다.
# 입출력 예 #4
# 다음과 같은 방법으로 황금 티켓 2개를 모을 수 있으며, 이보다 더 많은 황금 티켓을 모을 수 있는 방법이 없습니다.
# 1. 첫 번째 상점에서 "A" 3개를 구매하고 새로고침 합니다.
# 2. 두 번째 상점에서 "B" 2개를 구매하고 새로고침 합니다.
# 3. 세 번째 상점에서 "B" 1개를 구메합니다.
# "A" 3개, "B" 3개를 황금 티켓 2개와 교환할 수 있습니다.

from collections import defaultdict, deque


def solution(tickets, roll, shop, money):
    # 티켓 이름과 가격을 딕셔너리에 저장
    ticket_price = {}
    for ticket in tickets:
        name, price = ticket.split()
        ticket_price[name] = int(price)

    # 티켓 이름을 인덱스로 매핑
    ticket_indices = {name: idx for idx, name in enumerate(ticket_price.keys())}
    num_tickets = len(ticket_price)

    # DP 배열 초기화
    dp = defaultdict(lambda: defaultdict(int))

    # 초기 상태
    initial_state = (money, 0, tuple([0] * num_tickets))
    dp[money][tuple([0] * num_tickets)] = 0

    queue = deque([initial_state])

    # BFS 수행
    while queue:
        current_money, shop_index, ticket_counts = queue.popleft()

        # 현재 상태에서 만들 수 있는 최대 황금 티켓 수
        current_gold = dp[current_money][ticket_counts]

        # 최대 황금 티켓 수 갱신
        if shop_index >= len(shop):
            continue

        # 현재 상점에서 티켓 구매
        for ticket in shop[shop_index]:
            price = ticket_price[ticket]
            if current_money >= price:
                new_counts = list(ticket_counts)
                new_counts[ticket_indices[ticket]] += 1
                new_counts = tuple(new_counts)
                new_money = current_money - price
                new_gold = sum(count // 3 for count in new_counts)
                if dp[new_money][new_counts] < current_gold + new_gold:
                    dp[new_money][new_counts] = current_gold + new_gold
                    queue.append((new_money, shop_index, new_counts))

        # 상점을 새로고침
        if current_money >= roll and shop_index + 1 < len(shop):
            if dp[current_money - roll][ticket_counts] < current_gold:
                dp[current_money - roll][ticket_counts] = current_gold
                queue.append((current_money - roll, shop_index + 1, ticket_counts))

    # 최종 결과 계산
    max_gold_tickets = 0
    for remaining_money in dp:
        for ticket_counts in dp[remaining_money]:
            gold_tickets = dp[remaining_money][ticket_counts]
            max_gold_tickets = max(max_gold_tickets, gold_tickets)

    return max_gold_tickets


# 입출력 예시 테스트
print(solution(["A 1", "B 2", "C 5", "D 3"], 10, [["B", "C", "B", "C"], ["A", "A", "A", "B"], ["D", "D", "C", "D"]], 30)) # 2
print(solution(["A 1", "B 2", "C 5", "D 3"], 10, [["B", "C", "B", "C"], ["A", "A", "A", "B"], ["D", "D", "C", "D"]], 100)) # 4
print(solution(["A 2", "B 1"], 1, [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]], 9)) # 2
print(solution(["A 2", "B 1"], 5, [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]], 19)) # 2