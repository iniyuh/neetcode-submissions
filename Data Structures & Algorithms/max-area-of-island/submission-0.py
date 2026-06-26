class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        current_max = 0
        explored = set()

        def explore(i, j):
            size = 0

            if grid[i][j] == 1 and (i, j) not in explored:
                explored.add((i,j))
                size += 1

                if 0 < i: size += explore(i-1, j)
                if 0 < j: size += explore(i, j-1)
                if i+1 < len(grid): size += explore(i+1, j)
                if j+1 < len(grid[0]): size += explore(i, j+1)
            
            return size


        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1 and (i, j) not in explored:
                    current_max = max(explore(i,j), current_max)
        
        return current_max
