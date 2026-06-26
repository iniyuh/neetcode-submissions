class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(dict)
        for u, v, t in times:
            adjList[u][v] = t
        
        reached = set()
        queue = [(0, k)]

        while queue:
            t, u = heapq.heappop(queue)

            if u not in reached:
                reached.add(u)

                if len(reached) == n: return t

                for v in adjList[u].keys():
                    t_ = adjList[u][v]

                    heapq.heappush(queue, (t + t_, v))

        return -1