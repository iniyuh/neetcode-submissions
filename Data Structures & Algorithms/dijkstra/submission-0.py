class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        minHeap = []
        adjList = defaultdict(list)
        minHeap = []
        ret = {}

        for u, v, w in edges: 
            adjList[u].append((v, w))
        
        heapq.heappush(minHeap, (0, src))
        
        while minHeap:
            currentWeight, currentNode = heapq.heappop(minHeap)
            if currentNode in ret: continue

            ret[currentNode] = currentWeight

            for neighbor, edgeWeight in adjList[currentNode]:
                if neighbor not in ret:
                    heapq.heappush(minHeap, (currentWeight + edgeWeight, neighbor))

        for node in range(n):
            if node not in ret: ret[node] = -1

        return ret


