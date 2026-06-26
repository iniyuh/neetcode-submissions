# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxDepth = 0
        ret = None
        
        def dfs(depth, node):
            if not node: return (False, False)

            p1, q1 = dfs(depth + 1, node.left)
            p2, q2 = dfs(depth + 1, node.right)

            a, b = node.val == p.val or p1 or p2, node.val == q.val or q1 or q2

            if a and b: 
                print("dsfajl")
                nonlocal maxDepth
                nonlocal ret

                if depth > maxDepth:
                    maxDepth = depth
                    ret = node
            
            return (a, b)

        dfs(1, root)
        return ret
        


        