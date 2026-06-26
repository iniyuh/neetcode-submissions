class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums): return 0
            elif i in memo: return memo[i]
            else:
                ret = max(
                    nums[i] + dfs(i + 2), 
                    dfs(i + 1)
                )
                memo[i] = ret
                return ret
        
        return dfs(0)