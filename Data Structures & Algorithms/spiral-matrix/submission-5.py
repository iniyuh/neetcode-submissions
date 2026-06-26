class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        i, j = 0, 0
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        currDirection = 0
        di, dj = deltas[0]
        res = []

        while True:
            if (i, j) not in visited and i < len(matrix) and -1 < i and j < len(matrix[0]) and -1 < j:
                res.append(matrix[i][j])
                visited.add((i, j))
                i += di
                j += dj
            else:
                i -= di
                j -= dj

                currDirection = (currDirection + 1) % 4
                di, dj = deltas[currDirection]

                i += di
                j += dj

                if (i, j) in visited or i < 0 or len(matrix) == i or j < 0 or len(matrix[0]) == j: break
        
        return res



