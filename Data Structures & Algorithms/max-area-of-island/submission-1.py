class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        blacklist = set()
        maxArea = 0

        def explore(r, c):
            if (
                r == -1 or
                c == -1 or
                r == R or
                c == C or
                grid[r][c] == 0 or
                (r, c) in blacklist
            ): return 0

            area = 1
            blacklist.add((r, c))

            for dr, dc in directions:
                area += explore(r+dr, c+dc)
            
            return area
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in blacklist:
                    maxArea = max(maxArea, explore(r, c))
        
        return maxArea
