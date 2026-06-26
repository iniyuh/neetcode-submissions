class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialize count to 0
        # create adjList
        # create quota set of all nodes
        # while quota
            # dfs node in quota
                # for each node we reach, remove from quota 
            # increment count
        
        count = 0
        adjList = defaultdict(list)
        quota = set()

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        for node in range(n): quota.add(node)

        def dfs(node):
            print("checking", node)
            if node not in quota: return
            print("found", node)


            quota.remove(node)
            for neighbor in adjList[node]:
                dfs(neighbor)

        print(quota)

        while quota:
            print("attempt", count)
            node = next(iter(quota))
            print(node)
            dfs(node)
            count += 1
        
        return count
        


