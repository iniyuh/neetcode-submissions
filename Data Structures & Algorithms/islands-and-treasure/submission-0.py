class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # loop through grid
            # if cell is treasure chest
                # propagate out distances from here
                    # stop propagating if we hit water, the edge of the grid or a shorter distance

        INF = 2147483647
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))


        def propagate(currDistance, r, c):
            if (
                r == -1 or
                c == -1 or
                r == R or
                c == C or
                grid[r][c] <= currDistance
            ): return

            print(r, c, "becomes:", currDistance)
            grid[r][c] = currDistance

            for dr, dc in directions:
                propagate(currDistance + 1, r+dr, c+dc)
            

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    print("hit", r, c)
                    for dr, dc in directions:
                        propagate(1, r+dr, c+dc)
        
        return
