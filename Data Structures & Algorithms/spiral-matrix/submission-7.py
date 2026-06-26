class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        R, C = len(matrix), len(matrix[0])
        N = R * C
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 0

        r, c = 0, 0
        count = 0
        visited = set()
        ret = []

        def nav(r, c):
            nonlocal dirIdx
            
            dr, dc = directions[dirIdx]
            nr, nc = r+dr, c+dc
            print((nr, nc))

            if (nr, nc) in visited or nr == -1 or nc == -1 or nr == R or nc == C:
                dirIdx = (dirIdx + 1) % 4
                dr, dc = directions[dirIdx]
                print("new dirIdx", dirIdx)
                print("new dir", dr, dc)
                print("adjusted to ", (r+dr, c+dc))
                return (r+dr, c+dc)

            print("allowed")
            return (nr, nc)


        

        while count < N:
            ret.append(matrix[r][c])
            visited.add((r, c))
            count += 1

            r, c = nav(r, c)
        
        return ret