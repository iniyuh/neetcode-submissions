"""
Generate adjacency lists O(n)

    Sort adjacency lists O(n)
    DFS in lexicographical order (brute force) O(n^2)
        Try each "ticket" by removing it, adding the airport to our path and 
        going down a level
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for src, dst in tickets:
            adjList[src].append(dst)
        
        for key in adjList.keys():
            adjList[key].sort()

        path = ["JFK"]

        def dfs():
            if len(path) == len(tickets) + 1: return True

            src = path[-1]

            for i, dst in enumerate(adjList[src]):
                path.append(dst)
                adjList[src].pop(i)

                if dfs(): return True

                path.pop()
                adjList[src].insert(i, dst)
            
            return False

        dfs()
        return path
