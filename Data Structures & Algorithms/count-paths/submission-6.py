class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for c in range(n)] for r in range(m)]
        def dfs(r, c):
            if r == m - 1 or c == n - 1: return 1
            elif memo[r][c] != -1: return memo[r][c]
            else:
                memo[r][c] = dfs(r+1, c) + dfs(r, c+1)
                return memo[r][c]

        return dfs(0, 0)