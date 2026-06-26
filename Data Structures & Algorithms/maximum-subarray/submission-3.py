class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0

        for num in nums:
            if sum < 0: sum = 0

            sum += num

            maxSum = max(maxSum, sum)
        
        return maxSum
