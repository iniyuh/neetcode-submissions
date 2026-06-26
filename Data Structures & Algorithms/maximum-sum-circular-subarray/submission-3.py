class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, localMax = nums[0], 0
        globalMin, localMin = nums[0], 0

        total = 0
        
        for num in nums:
            localMax += num
            localMin += num

            globalMax, globalMin = max(globalMax, localMax), min(globalMin, localMin)

            if localMax < 0: localMax = 0
            if localMin > 0: localMin = 0

            total += num


        if globalMax < 0: return globalMax
        else: return max(globalMax, total - globalMin)
