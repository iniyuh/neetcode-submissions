# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        ans = []
        currQ = [root]

        while currQ:
            levelList = []
            nextQ = []

            for node in currQ:
                levelList.append(node.val)
                if node.left: nextQ.append(node.left)
                if node.right: nextQ.append(node.right)
            
            ans.append(levelList)

            currQ = nextQ
        
        return ans