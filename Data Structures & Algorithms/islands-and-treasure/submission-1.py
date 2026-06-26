class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


        queue = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: 
                    queue.append(((r, c), -1))
        

        while queue:
            (r, c), d = queue.popleft()

            if d == -1 or grid[r][c] == 2147483647:
                if d == -1: d = 0

                grid[r][c] = d

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (
                        nr != R and
                        nr != -1 and
                        nc != C and 
                        nc != -1 and
                        grid[nr][nc] == 2147483647
                    ):
                        queue.append(((nr, nc), d + 1))