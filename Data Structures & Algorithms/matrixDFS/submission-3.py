class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = set()

        def dfs(r, c):
            if (
                r == -1 or 
                c == -1 or 
                r == R or
                c == C or
                (r, c) in visited or
                grid[r][c] == 1
            ): return 0
            elif r == R - 1 and c == C - 1: return 1
            else:
                visited.add((r, c))
                ret = 0
                for dr, dc in directions:
                    ret += dfs(r+dr, c+dc)
                visited.remove((r, c))
                return ret
        
        return dfs(0, 0)
