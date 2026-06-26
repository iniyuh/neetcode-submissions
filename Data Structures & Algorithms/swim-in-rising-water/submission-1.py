class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # analagous to cell value is "edge weight", with a greedy approach
        # however we do not keep track of total "path length", just the max weight on our min path
        # keep taking "shortest edge" until we reach bottom right

        N = len(grid)
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        start, end = (0, 0), (N-1, N-1)

        r, c = start 
        maxTime = 0
        minHeap = [(0, (0, 0))]
        visited = set()

        while minHeap:
            time, (r, c) = heapq.heappop(minHeap)

            maxTime = max(maxTime, grid[r][c])
            visited.add((r, c))

            if (r, c) == end: break

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if nr != -1 and nc != -1 and nr != N and nc != N and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (grid[nr][nc], (nr, nc)))
        
        return maxTime




