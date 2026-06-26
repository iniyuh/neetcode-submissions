class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, i):
        if self.par[i] == i: return i
        else: 
            self.par[i] = self.find(self.par[i])
            return self.par[i]
    
    def union(self, i, j):
        rootI, rootJ = self.find(i), self.find(j)

        if rootI == rootJ: 
            return False
        else:
            if self.rank[rootI] < self.rank[rootJ]:
                self.par[rootI] = rootJ
            elif self.rank[rootJ] < self.rank[rootI]:
                self.par[rootJ] = rootI
            else:
                self.rank[rootI] += 1
                self.par[rootJ] = rootI
            
            return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        uf = UnionFind(n)

        for a, b in edges:
            if not uf.union(a, b): return False
        
        return True



