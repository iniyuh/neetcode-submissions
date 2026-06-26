# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates = []
        def dfs(curr, target):
            if not curr: return
            elif curr.val == target:
                candidates.append(curr)

            dfs(curr.left, target)
            dfs(curr.right, target)
        
        def checkSame(a, b):
            if not a and not b: return True
            elif not a and b or not b and a: return False
            else: return a.val == b.val and checkSame(a.left, b.left) and checkSame(a.right, b.right)
        
        dfs(root, subRoot.val)
        for candidate in candidates:
            if checkSame(candidate, subRoot): return True
        
        return False
        
        