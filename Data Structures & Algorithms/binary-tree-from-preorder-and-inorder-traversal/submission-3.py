# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None

        rootNode = TreeNode(preorder[0])

        inorderRootIndex = inorder.index(preorder[0])
        
        leftInorder = inorder[:inorderRootIndex]
        rightInorder = inorder[inorderRootIndex+1:] if inorderRootIndex + 1 < len(inorder) else []
        leftPreorder = None
        rightPreorder = None

        if not leftInorder:
            rightPreorder = preorder[1:]
        elif not rightInorder:
            leftPreorder = preorder[1:]
        else:
            divider = 1
            while preorder[divider] in leftInorder: divider += 1
            leftPreorder = preorder[1:divider] 
            rightPreorder = preorder[divider:]

        rootNode.left = self.buildTree(leftPreorder, leftInorder)
        rootNode.right = self.buildTree(rightPreorder, rightInorder)

        return rootNode