# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        
        ret = None

        def size(node):
            if not node: return 0

            return 1 + size(node.left) + size(node.right)
        
        def findKth(implicit, node):
            if not node: return

            smaller = implicit + size(node.left)
            
            if smaller == k - 1: 
                nonlocal ret
                ret = node.val
                return
            elif smaller > k - 1: 
                findKth(0, node.left)
            else:
                findKth(smaller + 1, node.right)
        
        findKth(0, root)
        return ret



