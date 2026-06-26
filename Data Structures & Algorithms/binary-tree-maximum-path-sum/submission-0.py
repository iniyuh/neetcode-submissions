# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = root.val

        def dfs(node):
            if not node: return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            nonlocal maxVal
            maxVal = max(maxVal, node.val + left + right)

            return node.val + max(0, dfs(node.left), dfs(node.right))
        
        dfs(root)

        return maxVal

