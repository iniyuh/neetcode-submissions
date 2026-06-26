class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for u, v in tickets:
            adjList[u].append(v)
        for u in adjList.keys():
            adjList[u].sort(reverse=True)
        
        stack = ["JFK"]
        ret = []

        while stack:
            node = stack[-1]

            if not adjList[node]: 
                ret.append(node)
                stack.pop()
            else:
                stack.append(adjList[node].pop())
            
        return ret[::-1]

