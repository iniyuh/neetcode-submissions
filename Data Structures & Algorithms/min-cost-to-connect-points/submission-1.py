class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = [i for i in range(len(points))]
        rank = [0 for _ in range(len(points))]

        def find(i):
            if par[i] == i: return i
            else: 
                par[i] = find(par[i])
                return par[i]
        
        def union(i, j):
            a, b = find(i), find(j)

            if a == b: return False

            if rank[a] == rank[b]:
                rank[a] += 1
                par[b] = a
            elif rank[a] < rank[b]:
                par[a] = b
            else: par[b] = a

            return True
        
        minHeap = []
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                heapq.heappush(minHeap, (abs(xi - xj) + abs(yi - yj), i, j))

        ret = 0
        while minHeap:
            dist, i, j = heapq.heappop(minHeap)

            if union(i, j): ret += dist
        
        return ret
        


        