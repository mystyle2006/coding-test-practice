# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.

 

# Example 1:

# Input: nums = [3,5,2,1,6,4]
# Output: [3,5,1,6,2,4]
# Explanation: [1,6,2,5,3,4] is also accepted.
# Example 2:

# Input: nums = [6,6,5,6,3,8]
# Output: [6,6,5,6,3,8]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 104
# It is guaranteed that there will be an answer for the given input nums.

# 1) 0: nums[0] <= nums[1]
# 2) 1: nums[1] >= nums[2]
# 3) 2: nums[2] <= nums[3]
# 4) 3: nums[3] >= nums[4]
# 5) 4: nums[4] <= nums[5]
# -> even: nums[i] <= nums[i+1]
# -> odd: nums[i] >= nums[i+1]
class Solution:
    def swap(self, nums: List[int], _from: int, _to: int):
        nums[_from], nums[_to] = nums[_to], nums[_from]

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx, num in enumerate(nums[:-1]):
            print(idx, num)
            # when even and nums[idx] is larger than nums[idx+1]
            if idx % 2 == 0 and nums[idx] > nums[idx + 1]:
                self.swap(nums, idx, idx + 1)
            elif idx % 2 != 0 and nums[idx] < nums[idx + 1]:
                self.swap(nums, idx, idx + 1)
            


        
