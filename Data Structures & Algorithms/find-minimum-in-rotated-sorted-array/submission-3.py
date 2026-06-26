class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        prev = nums[-1]
        for num in nums:
            if num < prev: return num
            prev = num