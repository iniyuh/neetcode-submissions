"""
We run dfs with a param for max so far, 
    if the node value is gte we return 1 + dfs of branches (with updated max)
    else 0 + dfs of branches (with updated max)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currMax):
            if not node: return 0

            ret = 1 if node.val >= currMax else 0
            currMax = max(currMax, node.val)
            ret += dfs(node.left, currMax)
            ret += dfs(node.right, currMax)

            return ret
        
        return dfs(root, float('-inf'))