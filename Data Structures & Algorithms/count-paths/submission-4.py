class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for c in range(n)] for r in range(m)]

        def helper(r, c):
            if r == m - 1 or c == n - 1: return 1
            elif memo[r][c] != -1: return memo[r][c]
            else:
                memo[r][c] = helper(r+1, c) + helper(r, c+1)
                return memo[r][c]
        
        return helper(0, 0)
