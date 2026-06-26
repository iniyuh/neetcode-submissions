class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(i):
            if par[i] == i: return i
            else:
                par[i] = find(par[i])
                return par[i]
        
        def union(i, j):
            a, b = find(i), find(j)

            if a == b: return

            if rank[a] == rank[b]:
                rank[a] += 1
                par[b] = a
            elif rank[a] < rank[b]:
                par[a] = b
            else:
                par[b] = a

        for a, b in edges:
            union(a, b)
        
        count = 0
        for i in range(n):
            if par[i] == i: count += 1
        
        return count
            

