class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        N = R * C

        def value(n):
            return matrix[n // C][n % C]
        
        l, r = 0, N - 1

        while l <=r:
            m = (l + r) // 2

            val = value(m)

            if val == target: return True
            elif val < target: l = m + 1
            else: r = m - 1

        return False