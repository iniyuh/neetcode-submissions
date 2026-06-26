class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        visited = set()

        def dfs(r, c, prev):
            if r == -1 or r == R or c == -1 or c == C or (r, c) in visited or matrix[r][c] <= prev: return 0

            visited.add((r, c))
            ret = 0

            for dr, dc in directions:
                ret = max(ret, dfs(r+dr, c+dc, matrix[r][c]))
            
            visited.remove((r, c))
            return ret + 1
            

        ret = 0
        for r in range(R):
            for c in range(C):
                ret = max(ret, dfs(r, c, -1))
        
        return ret
