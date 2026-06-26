class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def propagate(currDist, r, c):
            if (
                r == -1 or
                c == -1 or
                r == R or
                c == C or
                grid[r][c] == 2 or
                grid[r][c] == 0 
            ): return
            
            if grid[r][c] == 1 or currDist > grid[r][c]:

                print("turned", r, c)
                grid[r][c] = currDist

                for dr, dc in directions:
                    propagate(currDist - 1, r+dr, c+dc)

            
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    print("spreading from", r, c)
                    for dr, dc in directions:
                        propagate(-1, r+dr, c+dc)


        minVal = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1: 
                    print("safe at", r, c)
                    return -1
                minVal = min(minVal, grid[r][c])

        return -1 * minVal
        