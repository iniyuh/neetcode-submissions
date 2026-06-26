# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currentMax):
            res = 0

            if node.val >= currentMax:
                res += 1
                currentMax = node.val
            
            if node.left: res += dfs(node.left, currentMax)
            if node.right: res += dfs(node.right, currentMax)

            return res
        
        return dfs(root, root.val)