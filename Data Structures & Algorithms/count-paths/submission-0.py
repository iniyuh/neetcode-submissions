class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * m

        for j in range(n - 1, -1, -1):
            currRow = [0] * m
            currRow[m-1] = 1
            for i in range(m - 2, -1, -1):
                currRow[i] = currRow[i+1] + prevRow[i]

            prevRow = currRow
            if j == 0: return currRow[0]