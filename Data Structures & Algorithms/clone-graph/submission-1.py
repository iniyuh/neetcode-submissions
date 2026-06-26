"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node'], log: dict=None) -> Optional['Node']:
        if not node: return None
        if not log: log = {}

        
        if node.val in log: return log[node.val]

        curr = Node(node.val)
        log[curr.val] = curr

        for neighbor in node.neighbors:
            curr.neighbors.append(self.cloneGraph(neighbor, log))
        
        return curr
