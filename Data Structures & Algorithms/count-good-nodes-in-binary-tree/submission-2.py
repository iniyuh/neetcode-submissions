# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        
        def dfs(currMax, node):
            if not node: return

            if node.val >= currMax:
                nonlocal count
                count += 1
                currMax = node.val
            dfs(currMax, node.left)
            dfs(currMax, node.right)
        
        dfs(float('-inf'), root)
        return count