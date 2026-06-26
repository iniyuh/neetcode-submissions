class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        quota = set()
        for i in range(n):
            quota.add(i)

        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(prev, node):
            print(prev, node, quota)
            if node not in quota: return False

            quota.remove(node)

            for neighbor in adjList[node]:
                if neighbor != prev: 
                    if not dfs(node, neighbor): return False

            return True
        
        if not dfs(-1, 0): return False
        return len(quota) == 0