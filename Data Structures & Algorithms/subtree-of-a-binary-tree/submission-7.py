# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: return False

        def matcher(node1, node2):
            if not node1 and not node2: return True
            elif not node1 or not node2: return False
            elif node1.val != node2.val: 
                print("matcher", node1.val, node2.val)
                return False
            else:
                print("matcher", node1.val, node2.val)
                return matcher(node1.left, node2.left) and matcher(node1.right, node2.right)
        
        def dfs(node):
            if not node: 
                print("null")
                return False
            else:
                if node.val == subRoot.val and matcher(node, subRoot): return True

                return dfs(node.left) or dfs(node.right)
        




        return dfs(root)

