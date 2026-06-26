class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        N = R * C
        print(R, C, N)
        
        def calcIndices(n):
            r = int(n / C)
            c = int(n % C)
            return (r, c)

        l, r = 0, N - 1

        while l <= r:
            m = (l + r) // 2
            row, col = calcIndices(m)
            val = matrix[row][col]

            print("l:", l, "r:", r, "m:", m, "val:", val)

            if val == target: return True
            elif target < val: r = m - 1
            else: l = m + 1

        return False 
