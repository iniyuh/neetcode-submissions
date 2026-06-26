# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        parent = None
        target = root

        while target and target.val != key:
            parent = target

            if target.val < key: target = target.right
            else: target = target.left
        
        # Key not in the tree
        if not target: return root

        # Target no children
        if not target.left and not target.right: 
            if not parent: return None

            if key < parent.val: parent.left = None
            else: parent.right = None

            return root
        
        # Target has children
        if target.left:
            prev = target
            replacement = target.left

            while replacement.right: 
                prev = replacement
                replacement = replacement.right

            if replacement.val < prev.val: prev.left = None
            else: prev.right = None

            target.val = replacement.val
            return root
        else:
            prev = target
            replacement = target.right

            while replacement.left: 
                prev = replacement
                replacement = replacement.left

            if replacement.val < prev.val: prev.left = None
            else: prev.right = None

            target.val = replacement.val
            return root


