class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0: return 0

        if m < n: m, n = n, m

        prev = [0] * n
        arr = []

        for _ in range(m):
            curr = [1] * n

            for i in range(n - 2, -1, -1):
                curr[i] = prev[i] + curr[i + 1]
            prev = curr

        return prev[0]
