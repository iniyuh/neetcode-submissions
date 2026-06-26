class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def calcWithout(ignoreIndex):
            weight = 0
            minHeap = [(0, 0)]
            adjList = [[] for _ in range(n)]
            for i, (u, v, w) in enumerate(edges):
                if i != ignoreIndex:
                    adjList[u].append((w, v))
                    adjList[v].append((w, u))
            visited = set()

            while minHeap and len(visited) < n:
                dist, node = heapq.heappop(minHeap)

                if node in visited: continue

                visited.add(node)
                weight += dist

                for distance, neighbor in adjList[node]:
                    heapq.heappush(minHeap, (distance, neighbor))
            
            return weight if len(visited) == n else -1

        def calcWith(forcedEdgeIndex):
            weight = 0
            minHeap = []
            adjList = [[] for _ in range(n)]
            for i, (u, v, w) in enumerate(edges):
                adjList[u].append((w, v))
                adjList[v].append((w, u))
            visited = set()
            a, b, w = edges[forcedEdgeIndex]
            visited.add(a)
            visited.add(b)
            weight += w

            for distance, neighbor in adjList[a]:
                    heapq.heappush(minHeap, (distance, neighbor))

            for distance, neighbor in adjList[b]:
                    heapq.heappush(minHeap, (distance, neighbor))


            while len(visited) < n:
                dist, node = heapq.heappop(minHeap)

                if node in visited: continue

                visited.add(node)
                weight += dist

                for distance, neighbor in adjList[node]:
                    heapq.heappush(minHeap, (distance, neighbor))
            
            return weight

        mstWeight = calcWithout(-1)
        ret = [[],[]]
        for i in range(len(edges)):
            weight = calcWithout(i)

            if weight > mstWeight or weight == -1: 
                ret[0].append(i)
                continue

            weight = calcWith(i)

            if weight == mstWeight: ret[1].append(i)
        
        return ret

