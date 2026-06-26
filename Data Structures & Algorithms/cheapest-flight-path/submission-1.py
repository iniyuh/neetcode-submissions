class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]
        for u, v, w in flights:
            adjList[u].append((v, w))
        
        minHeap = [(0, src, -1)]
        visited = set()

        while minHeap:
            weight, u, count = heapq.heappop(minHeap)
        
            if u == dst: return weight

            if count != k:
                for v, w in adjList[u]:
                    heapq.heappush(minHeap, (weight + w, v, count + 1))

        
        return -1

