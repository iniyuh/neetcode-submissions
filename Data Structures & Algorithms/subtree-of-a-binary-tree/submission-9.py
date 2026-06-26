# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameStructure(node1, node2):
            if not node1 and not node2: return True
            elif node1.val != node2.val: return False
            elif (node1.left is None) ^ (node2.left is None): return False
            elif (node1.right is None) ^ (node2.right is None): return False
            else: 
                return sameStructure(node1.left, node2.left) and sameStructure(node1.right, node2.right)

        
        def dfs(node):
            if not node: return False
            if node.val == subRoot.val: 
                if sameStructure(node, subRoot): return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
