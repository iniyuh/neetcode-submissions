class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, 0)]
        total = 0

        while len(visited) < len(points):
            dist, idx = heapq.heappop(minHeap)
            if idx in visited: continue

            visited.add(idx)
            total += dist
            ox, oy = points[idx]

            for i, (x, y) in enumerate(points):
                if i not in visited:
                    heapq.heappush(minHeap, (abs(x-ox) + abs(y-oy), i))
        
        return total

        
