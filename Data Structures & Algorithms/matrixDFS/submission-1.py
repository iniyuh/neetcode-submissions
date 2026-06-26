class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j) -> int:
            if grid[i][j] == 1 or (i,j) in visited: return 0
            if i == len(grid) - 1 and j == len(grid[0]) - 1: return 1
            else:
                sum = 0
                visited.add((i,j))
                if 0 < i: sum += dfs(i-1, j)
                if 0 < j: sum += dfs(i, j-1)
                if i+1 < len(grid): sum += dfs(i+1, j)
                if j+1 < len(grid[0]): sum += dfs(i, j+1)
                visited.remove((i,j))
                return sum
        
        return dfs(0, 0)
