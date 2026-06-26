class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}

        for i in range(n):
            par[i] = i
            rank[i] = 0

        def find(x):
            if par[x] != x: par[x] = find(par[x])
            return par[x]

        def union(a, b):
            pA, pB = find(a), find(b)

            if pA == pB: return

            if rank[pA] == rank[pB]:
                rank[pA] += 1
                par[pB] = pA
            elif rank[pA] < rank[pB]: par[pA] = pB
            else: par[pB] = pA
        
        for a, b in edges: union(a, b)

        compSet = set()

        for i in range(n): compSet.add(find(i))

        return len(compSet)

