class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # airports are nodes
        # tickets are edges
        # JFK is start node
        # want to always pick the ticket with the "smallest" destination airport name available

        adjList = defaultdict(list)
        taken = defaultdict(set)
        for u, v in tickets: adjList[u].append(v)
        for u, _ in tickets: adjList[u].sort()

        flightPath = []
        
        def dfs(u):
            flightPath.append(u)

            if len(flightPath) == len(tickets) + 1: return True

            for i, v in enumerate(adjList[u]):
                if i not in taken[u]:
                    taken[u].add(i)
                    if dfs(v): return True
                    taken[u].remove(i)

            flightPath.pop()
            return False
        
        dfs("JFK")
        return flightPath
        


