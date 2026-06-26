class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, i):
        if self.par[i] == i: return i
        
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        pA, pB = self.find(a), self.find(b)

        if pA == pB: return

        if self.rank[pA] < self.rank[pB]:
            self.par[pA] = pB
        elif self.rank[pB] < self.rank[pA]:
            self.par[pB] = pA
        else:
            self.rank[pA] += 1
            self.par[pB] = pA


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        minHeap = []
        edgeCount = 0
        totalWeight = 0

        for u, v, w in edges:
            heapq.heappush(minHeap, (w, u, v))
        
        while minHeap and edgeCount < n - 1:
            w, u, v = heapq.heappop(minHeap)

            if not uf.isConnected(u, v): 
                uf.union(u, v)
                edgeCount += 1
                totalWeight += w
        
        return totalWeight if edgeCount == n - 1 else -1
            

            
            