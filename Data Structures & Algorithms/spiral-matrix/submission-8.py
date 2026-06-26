class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirIdx = 0
        visited = set()
        ret = []
        r, c = 0, 0

        while len(ret) != R*C:
            ret.append(matrix[r][c])
            visited.add((r, c))

            r_, c_ = r + directions[dirIdx][0], c + directions[dirIdx][1]

            if r_ == -1 or c_ == -1 or r_ == R or c_ == C or (r_, c_) in visited:
                dirIdx = (dirIdx + 1) % 4
                r_, c_ = r + directions[dirIdx][0], c + directions[dirIdx][1]
            
            r, c = r_, c_

        return ret


