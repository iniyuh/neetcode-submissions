class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        currSum = 0

        for num in nums:
            currSum += num
            currMax = max(currMax, currSum)
            if currSum < 0: currSum = 0
        
        return currMax