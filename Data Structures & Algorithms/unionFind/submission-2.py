class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.n = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if self.parent[x] == x: return x
        else:
            parent = self.find(self.parent[x])
            return parent

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False

        pX, pY = self.find(x), self.find(y)

        if self.rank[pX] == self.rank[pY]:
            self.rank[pX] += 1
            self.parent[pY] = pX
        elif self.rank[pX] < self.rank[pY]:
            self.parent[pX] = pY
        else:
            self.parent[pY] = pX
        
        return True

    def getNumComponents(self) -> int:
        count = 0
        
        for i in range(self.n):
            if self.find(i) == i: count += 1
        
        return count
