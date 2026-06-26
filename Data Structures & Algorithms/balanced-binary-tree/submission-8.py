# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        memo = {}
        
        def height(node):
            if not node: return 0
            elif node in memo: return memo[node]
            else:
                memo[node] = 1 + max(height(node.left), height(node.right))
                return memo[node]
        
        def dfs(node):
            if not node: return True
            else:
                l, r = height(node.left), height(node.right)
                if abs(l - r) > 1: return False
                else: return dfs(node.left) and dfs(node.right)
        
        return dfs(root)
        