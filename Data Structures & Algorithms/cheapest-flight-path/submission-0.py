class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]

        for source, destination, price in flights:
            adjList[source].append((destination, price))
        

        visited = set()

        def dfs(airport, distTraveled, stops):
            if airport == dst: return distTraveled
            if stops == k + 1: return float('inf')

            ret = float('inf')

            visited.add(airport)
            for connection, distance in adjList[airport]:
                if connection not in visited:
                    ret = min(dfs(connection, distTraveled + distance, stops + 1), ret)
            visited.remove(airport)

            return ret
        
        ans = dfs(src, 0, 0)
        return int(ans) if ans != float('inf') else -1