class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curr):
            if i == len(nums): return (curr == target) * 1
            elif (i, curr) in memo: return memo[(i, curr)]
            else:
                memo[(i, curr)] = dfs(i+1, curr - nums[i]) + dfs(i+1, curr + nums[i])
                return memo[(i, curr)]
        
        return dfs(0, 0)