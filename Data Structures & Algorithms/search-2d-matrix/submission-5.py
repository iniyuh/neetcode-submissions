class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = len(matrix[0])

        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            i = m // a
            j = m % a

            if matrix[i][j] < target:
                l = m + 1
            elif target < matrix[i][j]:
                r = m - 1
            else:
                return True
        
        return False