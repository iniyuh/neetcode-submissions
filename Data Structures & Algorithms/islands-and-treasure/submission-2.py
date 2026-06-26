class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        
        queue = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: queue.append((r, c, 0))
        
        while queue:
            r, c, dist = queue.popleft()

            if grid[r][c] == INF or grid[r][c] == 0:
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF:
                        queue.append((nr, nc, dist + 1))
        
