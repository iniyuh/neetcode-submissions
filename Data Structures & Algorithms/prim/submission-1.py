class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        vertices = {0}
        candidates = []
        for v, w in adjList[0]:
            heapq.heappush(candidates, (w, v))

        ret = 0
        
        while candidates:
            w, u = heapq.heappop(candidates)

            if u in vertices: continue
            print(u, w)

            vertices.add(u)
            ret += w

            for v, w in adjList[u]:
                heapq.heappush(candidates, (w, v))
        
        if len(vertices) != n: return -1
        return ret

