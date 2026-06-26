# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maxDepth = 0

        def explore(currDepth, node):
            nonlocal maxDepth
            maxDepth = max(maxDepth, currDepth)

            if node.left: explore(currDepth + 1, node.left)
            if node.right: explore(currDepth + 1, node.right)
        
        explore(1, root)

        return maxDepth