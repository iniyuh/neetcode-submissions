class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
        
        visited = set()
        ordering = []

        def dfs(u, path):
            if u in path: return False
            elif u in visited: return True

            path.add(u)

            for v in adjList[u]:
                if not dfs(v, path): return False
            
            path.remove(u)
            visited.add(u)
            ordering.append(u)

            return True

        for u in range(n):
            if not dfs(u, set()): return []
        
        ordering.reverse()
        return ordering

        # 3 1 0 