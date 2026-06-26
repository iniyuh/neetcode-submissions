# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        def invert(node):
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left: invert(node.left)
            if node.right: invert(node.right)

            return node

        return invert(root)