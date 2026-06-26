class UnionFind:
    
    def __init__(self, n: int):
        self.rank = {}
        self.par = {}

        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
        
        self.numComponents = n

    def find(self, x: int) -> int:
        if self.par[x] == x: return x

        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False

        pX, pY = self.find(x), self.find(y)

        if self.rank[pX] == self.rank[pY]:
            self.rank[pX] += 1
            self.par[pY] = pX
        elif self.rank[pX] > self.rank[pY]:
            self.par[pY] = pX
        elif self.rank[pY] > self.rank[pX]:
            self.par[pX] = pY
        
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents

