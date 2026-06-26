# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        stack = [root]
        visited = set()
        ret = []

        while stack:
            node = stack.pop()

            if node.left and node.left not in visited: 
                while node:
                    stack.append(node)
                    node = node.left
            elif node.right and node.right not in visited:
                stack.append(node)
                stack.append(node.right)
            else:
                ret.append(node.val)
                visited.add(node)
        
        return ret
            
            
                

            
            
            