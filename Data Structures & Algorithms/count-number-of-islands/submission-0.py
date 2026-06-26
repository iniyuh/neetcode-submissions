class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        explored = set()

        def explore(i: int, j: int) -> None:
            if (i, j) not in explored and grid[i][j] == '1':
                explored.add((i, j))
                if 0 < i: explore(i-1, j)
                if 0 < j: explore(i, j-1)
                if i+1 < len(grid): explore(i+1, j)
                if j+1 < len(grid[0]): explore(i, j+1)


        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1' and (i, j) not in explored:
                    explore(i, j)
                    count += 1
        
        return count
