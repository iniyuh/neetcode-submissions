class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum, maxSum = 0, nums[0]

        for num in nums:
            if currentSum < 0: currentSum = 0
            currentSum += num
            maxSum = max(maxSum, currentSum)
        
        return maxSum