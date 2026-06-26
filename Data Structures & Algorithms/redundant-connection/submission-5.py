class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [i for i in range(n + 2)]
        rank = [1] * (n + 1)

        def find(node):
            if par[node] == node: return node
            else:   
                par[node] = find(par[node])
                return par[node]
        
        def union(a, b):
            c, d = find(a), find(b)

            if c == d: return True
            
            if rank[c] == rank[d]:
                rank[c] += 1
                par[d] = c
            elif rank[c] < rank[d]:
                par[c] = d
            else:
                par[d] = c
            
            return False
        
        for a, b in edges:
            if union(a, b): return [a, b]
        
        
        
