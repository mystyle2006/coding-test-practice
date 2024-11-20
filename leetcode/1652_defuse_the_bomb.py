from typing import List


class Solution:
    def circular_array(self, arr: List[int], n: int):
        # 배열 길이
        size = len(arr)

        # 순환된 인덱스 구하기
        return arr[n % size]

    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return list(map(lambda i: 0, code))
        elif k > 0:
            return list(map(lambda i: sum(map(lambda j: (self.circular_array(code, j + 1)), range(i, i+k))), range(0, len(code))))
        elif k < 0:
            return list(map(lambda i: sum(map(lambda j: (self.circular_array(code, j - 1)), range(i, i+k, -1))), range(0, len(code))))

solution = Solution()
print(solution.decrypt([0, 0], 0))
print(solution.decrypt([5,7,1,4], 3))
print(solution.decrypt([2,4,9,3], -2))