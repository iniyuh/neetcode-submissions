class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n+1)]
        for u, v, t in times:
            adjList[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap and len(visited) < n:
            t1, u = heapq.heappop(minHeap)

            if u in visited: continue

            time = max(time, t1)
            visited.add(u)

            for v, t2 in adjList[u]:
                heapq.heappush(minHeap, (t2 + t1, v))

        
        return time if len(visited) == n else -1


