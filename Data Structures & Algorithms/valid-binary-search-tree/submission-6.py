# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lowerBound: float = float('-inf'), upperBound: float = float('inf')) -> bool:
        if not root: return True

        if not root.val < upperBound or not lowerBound < root.val: return False

        return self.isValidBST(root.left, lowerBound, root.val) and self.isValidBST(root.right, root.val, upperBound)


