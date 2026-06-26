# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS down and if a node is P return [True, SOMETHING] if it's Q
return [SOMETHING, True]

and the first node to get both positive signals is the LCA
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = None
        maxDepth = -1
        
        def dfs(node, depth=0):
            if not node: return (False, False)

            result1 = dfs(node.left)
            result2 = dfs(node.right)

            leadsToP = (node.val == p.val) | result1[0] | result2[0]
            leadsToQ = (node.val == q.val) | result1[1] | result2[1]

            nonlocal LCA, maxDepth
            if leadsToP and leadsToQ and depth > maxDepth:
                # nonlocal LCA, maxDepth
                LCA = node
                maxDepth = depth
            
            print(node.val, leadsToP, leadsToQ)
            return (leadsToP, leadsToQ)
    
        dfs(root)
        return LCA

            



            