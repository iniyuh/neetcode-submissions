class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        def findStartOfCycle(prev, node):
            if node in visited: return node
            else:
                visited.add(node)

                for neighbor in adjList[node]:
                    if neighbor != prev: 
                        val = findStartOfCycle(node, neighbor)
                        if val: return val

                return None
        
        cycle = set()
        def findAllNodesInCycle(startNode, prevNode, currNode):
            if currNode == startNode:
                return True
            else:
                cycle.add(currNode)
                
                for neighbor in adjList[currNode]:
                    if neighbor != prevNode and findAllNodesInCycle(startNode, currNode, neighbor): 
                        return True
                
                cycle.remove(currNode)
                return False
        
        start = findStartOfCycle(0, 1)
        print("Start", start)
        for neighbor in adjList[start]:
            if findAllNodesInCycle(start, start, neighbor): break
        cycle.add(start)

        print("Cycle nodes", cycle)

        for a, b in reversed(edges):
            print(a, b)
            if a in cycle and b in cycle: return [a, b]
                


            


                
