"""
Brute force:
    We can develop every 2 set parition O(n^2)
    For every partition we develop, we check if the set sums are equal
Memoization:
    Since brute force utilizes dfs based on: index, sum1, sum2, we can memoize 
    O(n * sum of nums)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i, sum1, sum2):
            if (i, sum1, sum2) in memo: return memo[(i, sum1, sum2)]
            if i == len(nums): return sum1 == sum2

            memo[(i, sum1, sum2)] = dfs(i+1, sum1 + nums[i], sum2) or dfs(i+1, sum1, sum2 + nums[i])
            return memo[(i, sum1, sum2)]
        
        return dfs(0, 0, 0)
