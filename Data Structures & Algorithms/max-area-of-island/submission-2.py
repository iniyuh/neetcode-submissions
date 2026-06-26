class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def calcArea(r, c):
            if r == -1 or c == -1 or r == R or c == C or grid[r][c] == 0 or (r, c) in visited: return 0
            else: 
                ret = 1
                visited.add((r, c))
                for dr, dc in directions: ret += calcArea(r+dr, c+dc)
                return ret

        maxArea = 0

        for r in range(R):
            for c in range(C):
                maxArea = max(maxArea, calcArea(r, c))

        return maxArea
