class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(i, curr):
            if i == len(nums): return curr == 0
            else:
                return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr - nums[i])

        return dfs(0, 0)
