class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:        
        n = len(edges)

        parent = {}
        rank = {}
        ret = None
        

        for i in range(1, n + 1):
            parent[i] = i
            rank[i] = 0


        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]



        for a, b in edges:
            p1, p2 = find(a), find(b)

            if p1 == p2: 
                ret = [a, b]
                continue

            if rank[p1] < rank[p2]: parent[p1] = p2
            elif rank[p2] < rank[p1]: parent[p2] = p1
            else: 
                parent[p1] = p2
                rank[p2] += 1
        
        return ret

