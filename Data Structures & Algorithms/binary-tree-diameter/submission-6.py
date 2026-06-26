# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):
            if not node: return 0
            else:
                left = 1 + maxDepth(node.left)
                right = 1 + maxDepth(node.right)
                span = left + right - 2
                print(node.val, "span", span)
                nonlocal maxSpan 
                maxSpan = max(maxSpan, span)
                return max(left, right)
        
        maxSpan = 0
        maxDepth(root)
        return maxSpan
