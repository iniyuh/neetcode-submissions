class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.R, self.C = len(matrix), len(matrix[0])
        N = self.R * self.C

        l, r = 0, N

        while l < r:
            m = (l + r) // 2

            val = self.getValue(matrix, m)

            if val == target: return True
            elif target < val: r = m
            else: l = m + 1
        
        return False
    
    def getValue(self, matrix, index):
        row = index // self.C
        col = index % self.C

        return matrix[row][col]