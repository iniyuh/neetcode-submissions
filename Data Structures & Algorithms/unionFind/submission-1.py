class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.n = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.par[x] == self.par[y]

    def union(self, x: int, y: int) -> bool:
        pX, pY = self.find(x), self.find(y)

        if pX == pY: return False
        else:
            if self.rank[pX] == self.rank[pY] or self.rank[pY] < self.rank[pX]:
                self.rank[pX] += 1
                self.par[pY] = pX
            else:
                self.rank[pY] += 1
                self.par[pX] = pY
            return True

    def getNumComponents(self) -> int:
        compSet = set()
        for i in range(self.n):
            compSet.add(self.find(i))
        
        return len(compSet)
