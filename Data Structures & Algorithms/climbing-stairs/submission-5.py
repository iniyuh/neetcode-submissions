class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            else:
                if i == n: return 1
                elif n < i: return 0
                else:
                    return dfs(i+1) + dfs(i+2)
        return dfs(0)