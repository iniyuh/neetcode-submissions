# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildNode(preorder, inorder):
            rootNode = TreeNode(preorder[0])

            leftLength = 0
            while inorder[leftLength] != rootNode.val: leftLength += 1

            preLeft = preorder[ 1 : 1 + leftLength ]
            preRight = preorder[ 1 + leftLength :]

            inLeft = inorder[ : leftLength ]
            inRight = inorder[ leftLength + 1 : ]

            if preLeft: rootNode.left = buildNode(preLeft, inLeft)
            if preRight: rootNode.right = buildNode(preRight, inRight)

            return rootNode
        
        return buildNode(preorder, inorder)
