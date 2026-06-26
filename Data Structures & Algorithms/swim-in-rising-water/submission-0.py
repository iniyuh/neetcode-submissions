class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        maxTime = 0
        minHeap = [(grid[0][0], (0, 0))]

        while minHeap:
            time, (r, c) = heapq.heappop(minHeap)

            maxTime = max(time, maxTime)
            grid[r][c] = -1

            if (r, c) == (R-1, C-1): return maxTime
            else:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if nr == -1 or nc == -1 or nr == R or nc == C or grid[nr][nc] == -1: continue
                    heapq.heappush(minHeap, (grid[nr][nc], (nr, nc)))



