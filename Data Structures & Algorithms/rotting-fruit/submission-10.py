"""
Scan matrix and count all fresh fruit, store all rotten fruit (seeds) O(n)
Multi source bfs from all rotten fruit until queue is empty O(n)
    Count how many fruit we spoil
After MSBFS is spoiled count != initial fresh count, return -1, otherwise minutes
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        minutes = 0
        queue = []
        freshFruit = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1: freshFruit += 1
                elif grid[r][c] == 2: 
                    for dr, dc in directions:
                        heapq.heappush(queue, (1, r+dr, c+dc))

        if freshFruit == 0: return 0
        
        while queue:
            t, r, c = heapq.heappop(queue)
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                grid[r][c] = 2
                freshFruit -= 1

                if freshFruit == 0: return t

                for dr, dc in directions:
                    heapq.heappush(queue, (t + 1, r+dr, c+dc))

        
        return -1