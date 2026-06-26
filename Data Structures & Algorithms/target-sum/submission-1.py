class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        def dfs(i, currentSum, target):
            if i == length - 1:
                if nums[i] == 0 and currentSum == target: return 2
                if currentSum + nums[i] == target or currentSum - nums[i] == target: return 1
                else: return 0
            else:
                return dfs(i + 1, currentSum + nums[i], target) + dfs(i + 1, currentSum - nums[i], target)
        
        return dfs(0, 0, target)

