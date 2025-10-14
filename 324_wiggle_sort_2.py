# rules
# 0: nums[0] < nums[1]
# 1: nums[1] > nums[2]
# 2: nums[2] < nums[3]
# 3: nums[3] > nums[4]
# if index is even: nums[i] < nums[i+1]
# if index is odd: nums[i] > nums[i+1]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) - 1) // 2
        # nums[::2] -> odd indices
        # nums[1::2] -> even indices
        # nums[mid::-1], nums[:mid:-1] -> assign the elements from the larger subarray to the even indices, and the elements from the smaller subarray to the odd indices
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
