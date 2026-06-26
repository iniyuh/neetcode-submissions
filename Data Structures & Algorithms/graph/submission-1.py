class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList: self.adjList[src] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def dfs(node):
            if node == dst: return True
            elif node in visited or node not in self.adjList: return False
            else:
                visited.add(node)

                for neighbor in self.adjList[node]:
                    if dfs(neighbor): return True
                
                visited.remove(node)
                return False
        
        ret = dfs(src)
        return ret