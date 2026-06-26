class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [0 for i in range(len(edges) + 1)]

        def find(i):
            if par[i] == i: return i
            else: 
                par[i] = find(par[i])
                return par[i]
        
        def union(i, j):
            a, b = find(i), find(j)

            if a == b: return True
            else:
                if rank[a] == rank[b]:
                    rank[a] += 1
                    par[b] = a
                elif rank[a] < rank[b]: par[a] = b
                else: par[b] = a
                
                return False
        
        for i, j in edges:
            if union(i, j): return [i, j]