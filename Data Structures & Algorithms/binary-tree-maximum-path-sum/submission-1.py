# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        maxSum = root.val

        def helper(node):
            nonlocal maxSum

            leftSum = helper(node.left) if node.left else 0
            rightSum = helper(node.right) if node.right else 0

            maxSum = max(maxSum, node.val, node.val + leftSum, node.val + rightSum, node.val + leftSum + rightSum)

            return node.val + max(0, leftSum, rightSum)
        
        helper(root)
        return maxSum