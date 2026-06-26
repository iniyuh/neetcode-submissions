class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)

        visited = set()
        currPath = set()
        topologicalSort = []

        def dfs(u):
            if u in currPath: return False
            if u in visited: return True

            visited.add(u)
            currPath.add(u)

            for v in adjList[u]:
                if not dfs(v): return False
            
            topologicalSort.append(u)
            currPath.remove(u)
            return True
        
        for u in range(n):
            if not dfs(u): return []
        
        topologicalSort.reverse()
        return topologicalSort



