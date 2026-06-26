class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [0] * n
        prev = [1] * n

        for _ in range(m-1):
            for c in range(n-1, -1, -1):
                curr[c] = prev[c] + (curr[c+1] if c+1 != n else 0)
            prev = curr

        return prev[0]