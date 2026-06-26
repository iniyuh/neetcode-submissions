# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = collections.deque()
        q.append(root)

        ret = []

        while q:
            x = []
            for i in range(len(q)):
                curr = q.popleft()
                x += [curr.val]
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ret.append(x)
        return ret