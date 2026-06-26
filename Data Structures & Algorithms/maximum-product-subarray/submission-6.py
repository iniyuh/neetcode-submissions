class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = nums[0]
        localMin = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp = max(localMax * num, localMin * num, num) # -24, 6, -2
            localMin = min(localMax * num, localMin * num, num) 
            localMax = temp
            globalMax = max(localMax, globalMax) # 12
            print(localMax, localMin)

        return globalMax

