class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i, curr):
            if (i, curr) in memo: return memo[(i, curr)]
            elif i == len(nums): return curr == 0
            else:
                memo[(i, curr)] = dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr - nums[i])
                return memo[(i, curr)]

        return dfs(0, 0)
