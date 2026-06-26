class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(i):
            if par[i] == i: return i
            else:
                par[i] = find(par[i])
                return par[i]
        
        def union(a, b):
            parA, parB = find(a), find(b)

            if parA == parB: return True
            else:
                if rank[parA] == rank[parB]:
                    rank[parA] += 1
                    par[parB] = parA
                elif rank[parA] < rank[parB]:
                    par[parA] = parB
                else:
                    par[parB] = parA
                
                return False
        
        for a, b in edges:
            if union(a, b): return [a, b]
