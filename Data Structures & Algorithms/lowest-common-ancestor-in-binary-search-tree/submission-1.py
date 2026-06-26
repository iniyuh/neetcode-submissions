# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = []
        path_q = []
        
        def findPath(node: TreeNode, path: list[TreeNode], targetVal: int):
            if not node: return False
            path.append(node)
            
            if node.val is targetVal: return True

            nextNode = node.left if targetVal < node.val else node.right
            if not findPath(nextNode, path, targetVal): 
                path.pop()
                return False
            
            return True
            
        
        findPath(root, path_p, p.val)
        findPath(root, path_q, q.val)
        print([node.val for node in path_p])
        print([node.val for node in path_q])


        while len(path_p) != len(path_q):
            if len(path_p) > len(path_q): path_p.pop()
            else: path_q.pop()
        
        while path_p[-1] != path_q[-1]: 
            path_p.pop()
            path_q.pop()
        
        return path_q[-1]

    




