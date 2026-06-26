class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        visited = set()

        for r in range(R):
            for c in range(C):
                if (r, c) in visited: continue

                if matrix[r][c] == 0: 

                    for r_ in range(R):
                        if matrix[r_][c] != 0: 
                            matrix[r_][c] = 0
                            visited.add((r_, c))

                    for c_ in range(C):
                        if matrix[r][c_] != 0: 
                            matrix[r][c_] = 0
                            visited.add((r, c_))
        
        return
                    
        