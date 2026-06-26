# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_value = preorder[0]
        left_tree_length = root_index_inorder = inorder.index(root_value)
        right_tree_length = len(inorder) - root_index_inorder - 1

        root_node = TreeNode(root_value)
        root_node.left = self.buildTree(preorder[1:1+left_tree_length], inorder[:root_index_inorder]) if left_tree_length > 0 else None
        root_node.right = self.buildTree(preorder[1+left_tree_length:], inorder[root_index_inorder+1:]) if right_tree_length > 0 else None

        return root_node