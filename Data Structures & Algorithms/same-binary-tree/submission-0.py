# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dualDfs(a, b):
            if not a: return not b
            if not b: return False
            if a.val != b.val: return False
            return dualDfs(a.left, b.left) and dualDfs(a.right, b.right)

        return dualDfs(p, q)