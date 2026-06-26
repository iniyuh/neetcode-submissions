# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currP, currQ = root, root
        ret = None

        while currP and currQ and currP == currQ:
            ret = currP
            print(ret.val)

            if p.val == currP.val: break
            elif p.val < currP.val: currP = currP.left
            else: currP = currP.right

            if q.val == currQ.val: break
            elif q.val < currQ.val: currQ = currQ.left
            else: currQ = currQ.right
        
        return ret