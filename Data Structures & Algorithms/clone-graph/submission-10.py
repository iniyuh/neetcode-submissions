"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldToNew = {}
        waitingOnOld = defaultdict(list)

        q = [node]
        ret = None

        while q:
            old = q.pop()

            if old in oldToNew: continue

            new = Node(old.val)
            oldToNew[old] = new

            if not ret: ret = new

            if old in waitingOnOld:
                for neighbor in waitingOnOld[old]:
                    neighbor.neighbors.append(new)

            for neighbor in old.neighbors:
                if neighbor in oldToNew: new.neighbors.append(oldToNew[neighbor]) 
                else:
                    waitingOnOld[neighbor].append(new)
                    q.append(neighbor)
        
        return ret
            

            
