class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        # curSum = 0
        minLength = float("inf")

        for r in range(1, len(nums) + 1):
            curSum = sum(nums[l:r])

            while curSum >= target:
                minLength = min(minLength, r - l)
                curSum -= nums[l]
                l += 1
                

        return minLength if minLength != float("inf") else 0