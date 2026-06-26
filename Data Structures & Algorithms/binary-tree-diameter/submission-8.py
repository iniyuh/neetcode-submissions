# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node):
            if not node.left and not node.right: return 1

            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, left + right)

            return 1 + max(left, right)

        
        dfs(root)
        return maxDiameter

