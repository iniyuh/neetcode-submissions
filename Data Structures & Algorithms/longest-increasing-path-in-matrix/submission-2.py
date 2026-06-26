"""
Brute force: from each cell determine the longest increasing path possible
    which is O(4^n) time and O(n) space which is in total O(n*4^n) time
Memoization? We would hav eto include the visited set. Memo space is 
    visited (n) * number of cells (n) so time is O(n^2) and space is O(n^2)
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        longestFrom = [[None for _ in range(C) ] for _ in range(R)] 

        globalMax = 0

        def helper(r, c):
            if longestFrom[r][c] is not None: return longestFrom[r][c]

            longestFrom[r][c] = 1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] > matrix[r][c]: 
                    longestFrom[r][c] = max(longestFrom[r][c], 1 + helper(nr, nc))
            
            nonlocal globalMax
            globalMax = max(globalMax, longestFrom[r][c])
            return longestFrom[r][c]
        

        for r in range(R):
            for c in range(C):
                helper(r, c)
        
        return globalMax
            

