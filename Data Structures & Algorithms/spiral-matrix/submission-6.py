class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        di, dj = 0, 1
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []

        while True:
            if right < left or bottom < top: break

            while left <= j and j <= right and top <= i and i <= bottom:
                res.append(matrix[i][j])
                print(matrix[i][j])
                i += di
                j += dj
            
            i -= di
            j -= dj

            if di == 0 and dj == 1: 
                top += 1
                di, dj = 1, 0
            elif di == 1 and dj == 0:
                right -= 1
                di, dj = 0, -1
            elif di == 0 and dj == -1:
                bottom -= 1
                di, dj = -1, 0
            else:
                left += 1
                di, dj = 0, 1
                
            i += di
            j += dj
        
        return res
            
