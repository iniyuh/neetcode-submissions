class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c):
            if r == m - 1 or c == n - 1: return 1
            else:
                return dfs(r+1, c) + dfs(r, c+1)

        return dfs(0, 0)