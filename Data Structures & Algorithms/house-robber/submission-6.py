"""
Brute force (DFS): O(2^n) time and O(n) space
Add memoization: O(n) time and O(n) space
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)

        def dfs(i):
            if i >= len(nums): return 0
            if memo[i] is not None: return memo[i]

            memo[i] = max( nums[i] + dfs(i + 2), dfs(i + 1) )
            return memo[i]
        
        return dfs(0)