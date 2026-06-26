class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.par = {}

        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    
    def find(self, u):
        if self.par[u] == u: return u

        self.par[u] = self.find(self.par[u])
        return self.par[u]
    
    def isSameComponent(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v):
        if self.isSameComponent(u, v): return False

        pU, pV = self.find(u), self.find(v)

        if self.rank[pU] == self.rank[pV]:
            self.rank[pU] += 1
            self.par[pV] = pU
        elif self.rank[pU] > self.rank[pV]:
            self.par[pV] = pU
        else:
            self.par[pU] = pV

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        
        for u, v in edges:
            if not uf.union(u-1, v-1): return [u, v]