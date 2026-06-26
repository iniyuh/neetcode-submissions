# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]):
        if not root: return []
        else:
            ret = []
            if root.left: ret += self.dfs(root.left)
            ret += [root.val]
            if root.right: ret += self.dfs(root.right)
            return ret
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root)[k-1]
        