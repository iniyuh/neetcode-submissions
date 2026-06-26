class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through all cells
            # if cell is 1 and not in blacklist 
                # explore entire island and mark in our blacklist
                # increment island counter

        # NOTES
        # Should be O(n) because we visit each cell exactly once.

        R, C = len(grid), len(grid[0])

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        blacklist = set()
        islandCounter = 0

        def explore(r, c, prefix):
            print(prefix, r, c)

            if (
                r == -1 
                or c == -1 
                or r == R 
                or c == C 
                or grid[r][c] == '0'
                or (r, c) in blacklist
            ): return

            print("PASS")
            blacklist.add((r, c))

            for dr, dc in directions:
                explore(r+dr, c+dc, prefix)



        

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r, c) not in blacklist:
                    islandCounter += 1
                    explore(r, c, "Island " + str(islandCounter) + ":")
        
        return islandCounter



            
