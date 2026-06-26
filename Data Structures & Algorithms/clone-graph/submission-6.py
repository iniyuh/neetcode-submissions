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

        hm = {}

        def helper(node):
            if node in hm: return hm[node]

            copy = Node(node.val)
            hm[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(helper(neighbor))
            
            return copy
        
        return helper(node)