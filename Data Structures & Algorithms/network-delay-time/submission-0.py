class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        quota = {i for i in range(1, n+1)}

        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))
        

        minHeap = [(0, k)]
        minTime = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node not in quota: continue
            else:
                quota.remove(node)
                minTime = time
                for v, t in adjList[node]:
                    heapq.heappush(minHeap, (time + t, v))
        
        return minTime if not quota else -1
        

