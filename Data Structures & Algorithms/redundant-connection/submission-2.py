class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for i in range(1, len(edges) + 1):
            par[i] = i
            rank[i] = 0
        
        def find(i):
            if par[i] != i: par[i] = find(par[i])
            return par[i]
        
        def add(x, y):
            pX, pY = find(x), find(y)

            if pX == pY: return False
            else:
                if rank[pX] == rank[pY]:
                    par[pY] = pX
                    rank[pX] += 1
                elif rank[pY] < rank[pX]: par[pY] = pX
                else: par[pX] = pY

                return True
        
        redundantEdge = None
        for a, b in edges:
            if not add(a, b): redundantEdge = [a, b]
        
        return redundantEdge