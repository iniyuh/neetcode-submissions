class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.prefix = [[0] * C for _ in range(R)]


        for r in range(R):
            rowSum = 0
            for c in range(C):
                rowSum += matrix[r][c]
                self.prefix[r][c] = rowSum + (self.prefix[r-1][c] if r > 0 else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefix[row2][col2]

        if row1 > 0: res -= self.prefix[row1 - 1][col2]
        if col1 > 0: res -= self.prefix[row2][col1 - 1]
        if row1 > 0 and col1 > 0: res += self.prefix[row1 - 1][col1 - 1]

        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)